/*
 * This file is part of CoAnSys project.
 * Copyright (c) 2012-2015 ICM-UW
 * 
 * CoAnSys is free software: you can redistribute it and/or modify
 * it under the terms of the GNU Affero General Public License as published by
 * the Free Software Foundation, either version 3 of the License, or
 * (at your option) any later version.

 * CoAnSys is distributed in the hope that it will be useful,
 * but WITHOUT ANY WARRANTY; without even the implied warranty of
 * MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE. See the
 * GNU Affero General Public License for more details.
 * 
 * You should have received a copy of the GNU Affero General Public License
 * along with CoAnSys. If not, see <http://www.gnu.org/licenses/>.
 */

/*
 * To change this license header, choose License Headers in Project Properties.
 * To change this template file, choose Tools | Templates
 * and open the template in the editor.
 */
package pl.edu.icm.coansys.source;

import java.io.IOException;
import java.util.ArrayList;
import java.util.Collections;
import java.util.Comparator;
import java.util.HashSet;
import org.apache.commons.lang.StringUtils;
import org.apache.hadoop.io.BytesWritable;
import org.apache.hadoop.io.Text;
import org.apache.hadoop.io.Writable;
import org.apache.hadoop.mapreduce.Reducer;
import pl.edu.icm.coansys.models.DocumentProtos;
import pl.edu.icm.coansys.models.ParentModelProtos;

/**
 *
 * @author kura
 */
public class ReduceDocsWithSameSourceId extends Reducer<Writable, BytesWritable, Text, BytesWritable> {

    @Override
    protected void reduce(Writable key, Iterable<BytesWritable> values, Context context) throws IOException, InterruptedException {
        ArrayList<String> docIds = new ArrayList<String>();
        HashSet<String> issns = new HashSet<String>();
        HashSet<String> isbns = new HashSet<String>();
        HashSet<String> titles = new HashSet<String>();
        for (BytesWritable value : values) {

            DocumentProtos.DocumentWrapper docWrapper = DocumentProtos.DocumentWrapper.parseFrom(value.copyBytes());
            docIds.add(docWrapper.getRowId());
            String issn = null;
            String isbn = null;
            if (docWrapper.hasDocumentMetadata() && docWrapper.getDocumentMetadata().hasBasicMetadata()) {
                DocumentProtos.BasicMetadataOrBuilder bm = docWrapper.getDocumentMetadata().getBasicMetadataOrBuilder();
                if (bm.hasIssn()) {
                    issn = bm.getIssn();
                }
                if (bm.hasIsbn()) {
                    isbn = bm.getIsbn();
                }
                if (StringUtils.isNotBlank(isbn)) {
                    isbn = isbn.trim().toUpperCase();
                    isbns.add(isbn);
                }
                if (StringUtils.isNotBlank(issn)) {
                    issn = issn.trim().toUpperCase();
                    issns.add(issn);
                }
                if (bm.hasJournal()) {
                    String title=bm.getJournal().trim();
                    if (StringUtils.isNotBlank(title)) {
                        titles.add(title);
                    }
                }
            }
           
        }
        String issn=null;
        String isbn=null;
        ArrayList<String> titleA=new ArrayList<String>(titles);
        Collections.sort(titleA, new Comparator<String>(){
            @Override
            public int compare(String o1, String o2) {
                //najdłuższe naprzód
                return o2.length()-o1.length();
            }
            
        });
        
        if (issns.size()>0) {
            issn=issns.iterator().next();
        }
        if (isbns.size()>0) {
            isbn=isbns.iterator().next();
        }
        String id="http://comac.ceon.pl/source-";
        if (issn!=null) {
            id+=("issn-"+issn);
            if (isbn!=null) {
                id+="-";
            }
        }
        if (isbn!=null) {
                id+=("isbn-"+isbn);
        }
        for (String docId:docIds){
            ParentModelProtos.ParentDisambiguationOut.Builder parent=ParentModelProtos.ParentDisambiguationOut.newBuilder();
            parent.setDocId(docId);
            parent.setParentId(id);
            parent.addAllParentName(titles);
            if (isbn!=null) {
                parent.setType(DocumentProtos.BasicMetadata.ParentType.BOOK);
            } else  {
                parent.setType(DocumentProtos.BasicMetadata.ParentType.JOURNAL);
            }
            context.write(new Text(docId), new BytesWritable(parent.build().toByteArray()));
        }
        
        
    }

}

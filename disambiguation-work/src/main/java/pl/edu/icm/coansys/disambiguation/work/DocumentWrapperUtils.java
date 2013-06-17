package pl.edu.icm.coansys.disambiguation.work;

import java.util.List;

import org.apache.hadoop.io.BytesWritable;
import org.apache.hadoop.io.Text;
import org.slf4j.Logger;
import org.slf4j.LoggerFactory;

import pl.edu.icm.coansys.importers.models.DocumentProtos;
import pl.edu.icm.coansys.importers.models.DocumentProtos.DocumentWrapper;

import com.google.common.collect.Lists;
import com.google.protobuf.InvalidProtocolBufferException;

/** 
 * Contains various utility methods related to DocumentWrapper class
 * @author lukdumi
 * 
 * */
public abstract class DocumentWrapperUtils {

    private static Logger log = LoggerFactory.getLogger(DocumentWrapperUtils.class);
    
    
    private DocumentWrapperUtils() {
        throw new IllegalStateException("a helper class, not to instantiate");
    }
    
    /** 
     * documentWrapper.getDocumentMetadata().getBasicMetadata().getTitle(0).getText() 
     * 
     * */
    public static String getMainTitle(DocumentWrapper documentWrapper) {
        return documentWrapper.getDocumentMetadata().getBasicMetadata().getTitle(0).getText();
    }
    
    /** 
     * Returns list of {@link DocumentWrapper}s parsed from values
     */
    public static List<DocumentWrapper> extractDocumentWrappers(Text key, Iterable<BytesWritable> values) throws InvalidProtocolBufferException {
        List<DocumentWrapper> documents = Lists.newArrayList();
        
        log.debug("--------\nkey: {}", key);
        for (BytesWritable value : values) {
            DocumentWrapper docWrapper = DocumentProtos.DocumentWrapper.parseFrom(value.copyBytes());
            log.debug("value: {}", docWrapper.getDocumentMetadata().getBasicMetadata().getTitle(0).getText());
            documents.add(docWrapper);
        }
        
        return documents;
    }
    
}
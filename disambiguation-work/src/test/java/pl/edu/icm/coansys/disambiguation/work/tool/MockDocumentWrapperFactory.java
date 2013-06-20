package pl.edu.icm.coansys.disambiguation.work.tool;

import java.util.List;
import java.util.UUID;

import pl.edu.icm.coansys.importers.models.DocumentProtos.Author;
import pl.edu.icm.coansys.importers.models.DocumentProtos.BasicMetadata;
import pl.edu.icm.coansys.importers.models.DocumentProtos.DocumentMetadata;
import pl.edu.icm.coansys.importers.models.DocumentProtos.DocumentWrapper;
import pl.edu.icm.coansys.importers.models.DocumentProtos.TextWithLanguage;

import com.beust.jcommander.internal.Lists;

public abstract class MockDocumentWrapperFactory {

    private MockDocumentWrapperFactory() {}
    
    public static DocumentWrapper changeTitle(DocumentWrapper docWrapper, int titleIndex, String newTitle) {
        BasicMetadata basicMetadata = docWrapper.getDocumentMetadata().getBasicMetadata();
        TextWithLanguage newTitle0 = TextWithLanguage.newBuilder(basicMetadata.getTitle(titleIndex)).setText(newTitle).build();
        BasicMetadata newBasicMetadata = BasicMetadata.newBuilder(basicMetadata).setTitle(titleIndex, newTitle0).build();
        DocumentMetadata newDocumentMetadata = DocumentMetadata.newBuilder(docWrapper.getDocumentMetadata()).setBasicMetadata(newBasicMetadata).build();
        DocumentWrapper newDocWrapper = DocumentWrapper.newBuilder(docWrapper).setDocumentMetadata(newDocumentMetadata).setRowId(docWrapper.getRowId()+UUID.randomUUID()).build();
        return newDocWrapper;
    }

    
    public static DocumentWrapper createDocumentWrapper(String title0) {
        TextWithLanguage textTitle0 = TextWithLanguage.newBuilder().setText(title0).build();
        BasicMetadata basicMetadata = BasicMetadata.newBuilder().addTitle(textTitle0).build();
        return createDocumentWrapper(basicMetadata);
    }
    
    public static DocumentWrapper createDocumentWrapper(String title0, int publicationYear, List<Author> authors) {
        TextWithLanguage textTitle0 = TextWithLanguage.newBuilder().setText(title0).build();
        BasicMetadata basicMetadata = BasicMetadata.newBuilder().addTitle(textTitle0).addAllAuthor(authors).setYear(""+publicationYear).build();
        return createDocumentWrapper(basicMetadata);
    }
    
    public static DocumentWrapper createDocumentWrapper(String title0, int publicationYear, Author... authors) {
        List<Author> authorList = Lists.newArrayList();
        for (Author author : authors) {
            authorList.add(author);
        }
        return createDocumentWrapper(title0, publicationYear, authorList);
    }
    
    public static DocumentWrapper createDocumentWrapper(BasicMetadata basicMetadata) {
        DocumentMetadata documentMetadata = DocumentMetadata.newBuilder().setKey(""+UUID.randomUUID()).setBasicMetadata(basicMetadata).build();
        DocumentWrapper docWrapper = DocumentWrapper.newBuilder().setDocumentMetadata(documentMetadata).setRowId(""+UUID.randomUUID()).build();
        return docWrapper;
        
    }
    
    public static Author createAuthor(String firstName, String lastName, int authorPosition) {
        Author author = Author.newBuilder().setKey(""+UUID.randomUUID()).setForenames(firstName).setSurname(lastName).setPositionNumber(authorPosition).build();
        return author;
    }
}

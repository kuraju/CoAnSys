/*
 * (C) 2010-2012 ICM UW. All rights reserved.
 */

package pl.edu.icm.coansys.citations.data

import collection.JavaConversions._
import pl.edu.icm.coansys.citations.util.misc._
import pl.edu.icm.coansys.commons.scala.strings
import pl.edu.icm.coansys.disambiguation.auxil.DiacriticsRemover._
import pl.edu.icm.cermine.bibref.BibReferenceParser
import pl.edu.icm.coansys.importers.models.DocumentProtos.{DocumentMetadata, BasicMetadata, ReferenceMetadata}
import pl.edu.icm.coansys.citations.data.CitationMatchingProtos.MatchableEntityData
import pl.edu.icm.cermine.bibref.model.BibEntry
import pl.edu.icm.coansys.citations.util.BytesConverter
import com.nicta.scoobi.core.Grouping

/**
 * @author Mateusz Fedoryszak (m.fedoryszak@icm.edu.pl)
 */
class MatchableEntity(val data: MatchableEntityData) {
  def id = data.getId

  def author = data.getAuthor

  def source = data.getSource

  def title = data.getTitle

  def pages = data.getPages

  def year = data.getYear

  def normalisedAuthorTokens: Iterable[String] =
    tokensFromCermine(strings.lettersOnly(removeDiacritics(author.toLowerCase)))
      .filter(_.length > 1)
      .map(_.toLowerCase)
      .toSet

  def toReferenceString: String = List(author, title, source, pages, year).mkString("; ")
}

object MatchableEntity {
  implicit val converter =
    new BytesConverter[MatchableEntity](
      (_.data.toByteArray),
      (x => new MatchableEntity(MatchableEntityData.parseFrom(x))))

  implicit val grouping = new Grouping[MatchableEntity] {
    def groupCompare(x: MatchableEntity, y: MatchableEntity) = x.id compareTo y.id
  }

  def fromBytes(bytes: Array[Byte]) = {
    new MatchableEntity(MatchableEntityData.parseFrom(bytes))
  }

  def fromParameters(id: String = "",
                     author: String = "",
                     source: String = "",
                     title: String = "",
                     pages: String = "",
                     year: String = "") = {
    val data = MatchableEntityData.newBuilder()
    data.setId(id)
    data.setAuthor(author)
    data.setSource(source)
    data.setTitle(title)
    data.setPages(pages)
    data.setYear(year)

    new MatchableEntity(data.build())
  }

  private def fillUsingBasicMetadata(data: MatchableEntityData.Builder, meta: BasicMetadata) {
    data.setAuthor(meta.getAuthorList.map(a => if (a.hasName) a.getName else a.getForenames + " " + a.getSurname).mkString(", "))
    data.setSource(meta.getJournal)
    data.setTitle(meta.getTitleList.map(_.getText).mkString(" "))
    data.setPages(meta.getPages)
    data.setYear(meta.getYear)
  }

  def fromDocumentMetadata(meta: DocumentMetadata) = {
    val data = MatchableEntityData.newBuilder()
    data.setId("doc_" + meta.getKey)
    fillUsingBasicMetadata(data, meta.getBasicMetadata)
    new MatchableEntity(data.build())
  }

  def fromReferenceMetadata(meta: ReferenceMetadata) = {
    val data = MatchableEntityData.newBuilder()
    data.setId("cit_" + meta.getSourceDocKey + "_" + meta.getPosition)
    fillUsingBasicMetadata(data, meta.getBasicMetadata)
    new MatchableEntity(data.build())
  }

  def fromUnparsedReferenceMetadata(bibReferenceParser: BibReferenceParser[BibEntry], meta: ReferenceMetadata) = {
    def getField(bibEntry: BibEntry, key: String): String =
      bibEntry.getAllFieldValues(key).mkString(" ")

    val bibEntry = bibReferenceParser.parseBibReference(removeDiacritics(meta.getRawCitationText))
    val data = MatchableEntityData.newBuilder()
    data.setId("cit_" + meta.getSourceDocKey + "_" + meta.getPosition)
    data.setAuthor(getField(bibEntry, BibEntry.FIELD_AUTHOR))
    data.setSource(getField(bibEntry, BibEntry.FIELD_JOURNAL))
    data.setTitle(getField(bibEntry, BibEntry.FIELD_TITLE))
    data.setPages(getField(bibEntry, BibEntry.FIELD_PAGES))
    data.setYear(getField(bibEntry, BibEntry.FIELD_YEAR))

    new MatchableEntity(data.build())
  }


}

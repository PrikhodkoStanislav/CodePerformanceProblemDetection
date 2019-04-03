package com.ground0.transaction.core.repository.db.util

import com.google.gson.JsonDeserializationContext
import com.google.gson.JsonDeserializer
import com.google.gson.JsonElement
import com.google.gson.JsonPrimitive
import com.google.gson.JsonSerializationContext
import com.google.gson.JsonSerializer
import org.threeten.bp.LocalDateTime
import org.threeten.bp.format.DateTimeFormatter
import java.lang.reflect.Type

/**
 * Created by 00-00-00 on 05/05/18.
 */

class LocalDateTimeConverter : JsonSerializer<LocalDateTime>, JsonDeserializer<LocalDateTime> {

  override fun serialize(src: LocalDateTime?, typeOfSrc: Type?, context: JsonSerializationContext?): JsonElement? {
    return JsonPrimitive(FORMATTER.format(src))
  }

  override fun deserialize(json: JsonElement?, typeOfT: Type?, context: JsonDeserializationContext?): LocalDateTime? {
    return FORMATTER.parse(json!!.asString, LocalDateTime.FROM)
  }

  companion object {
    private val FORMATTER = DateTimeFormatter.ISO_OFFSET_DATE_TIME
  }
}
package com.ground0.transaction.core.repository.db.util

import android.arch.persistence.room.TypeConverter
import org.threeten.bp.LocalDateTime

/**
 * Created by 00-00-00 on 05/05/18.
 */

open class DateTypeConverter {

  @TypeConverter
  fun toDate(value: String?): LocalDateTime = LocalDateTime.parse(value)

  @TypeConverter
  fun toString(value: LocalDateTime?): String = value.toString()

}
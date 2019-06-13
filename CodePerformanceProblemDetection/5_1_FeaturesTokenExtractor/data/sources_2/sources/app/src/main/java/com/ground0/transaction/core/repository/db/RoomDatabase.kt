package com.ground0.transaction.core.repository.db

import android.arch.persistence.room.Database
import android.arch.persistence.room.RoomDatabase
import android.arch.persistence.room.TypeConverters
import com.ground0.model.RetailTransaction
import com.ground0.transaction.core.repository.db.dao.RetailTransactionDao
import com.ground0.transaction.core.repository.db.util.DateTypeConverter

/**
 * Created by 00-00-00 on 05/05/18.
 */

@Database(entities = [(RetailTransaction::class)], version = 1)
@TypeConverters(DateTypeConverter::class)
abstract class RoomDatabase : RoomDatabase() {
  abstract fun transactionDao(): RetailTransactionDao
}
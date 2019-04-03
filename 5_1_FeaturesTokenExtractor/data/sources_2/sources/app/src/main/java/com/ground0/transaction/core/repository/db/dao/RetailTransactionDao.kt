package com.ground0.transaction.core.repository.db.dao

import android.arch.lifecycle.LiveData
import android.arch.persistence.room.Dao
import android.arch.persistence.room.Insert
import android.arch.persistence.room.OnConflictStrategy
import android.arch.persistence.room.Query
import com.ground0.model.RetailTransaction
import io.reactivex.Flowable

/**
 * Created by 00-00-00 on 05/05/18.
 */

@Dao
interface RetailTransactionDao {

  @Insert(onConflict = OnConflictStrategy.REPLACE)
  fun insert(retailTransaction: RetailTransaction)

  @Insert(onConflict = OnConflictStrategy.REPLACE)
  fun insert(retailTransactions: List<RetailTransaction>)

  @Query("SELECT * FROM retail_transactions WHERE id = :id LIMIT 1")
  fun getTransaction(id: Long): Flowable<RetailTransaction>

  @Query("SELECT * FROM retail_transactions")
  fun getTransactions(): Flowable<List<RetailTransaction>>

}
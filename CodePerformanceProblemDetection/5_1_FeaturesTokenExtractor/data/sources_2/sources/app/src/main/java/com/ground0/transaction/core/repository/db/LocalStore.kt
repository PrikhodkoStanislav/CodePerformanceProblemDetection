package com.ground0.transaction.core.repository.db

import android.arch.persistence.room.Room
import android.content.Context
import com.ground0.model.Customer
import com.ground0.model.RetailTransaction
import com.ground0.model.Retailer
import com.ground0.transaction.core.repository.Repository
import io.reactivex.Observable
import io.reactivex.schedulers.Schedulers

/**
 * Created by 00-00-00 on 05/05/18.
 */

object LocalStore : Repository {

  private lateinit var databaseImp: RoomDatabase

  fun init(context: Context) {
    databaseImp = Room.databaseBuilder(context, RoomDatabase::class.java, "transaction_db")
        .build()
  }

  override fun getTransactions(): Observable<List<RetailTransaction>> {
    return databaseImp.transactionDao()
        .getTransactions()
        .toObservable()
  }

  override fun getTransaction(id: Long): Observable<RetailTransaction> {
    return databaseImp.transactionDao()
        .getTransaction(id)
        .toObservable()
  }

  override fun postTransactions(retailTransactions: List<RetailTransaction>): Observable<Unit> {
    return Observable.fromCallable {
      databaseImp.transactionDao()
          .insert(retailTransactions)
    }
        .subscribeOn(Schedulers.io())
  }

  override fun postTransaction(retailTransaction: RetailTransaction): Observable<Unit> {
    return Observable.fromCallable {
      databaseImp.transactionDao()
          .insert(retailTransaction)
    }
        .subscribeOn(Schedulers.io())
  }

  override fun getCustomers(): Observable<List<Customer>> {
    TODO(
        "not implemented"
    ) //To change body of created functions use File | Settings | File Templates.
  }

  override fun postCustomers(customers: List<Customer>): Observable<Unit> {
    TODO(
        "not implemented"
    ) //To change body of created functions use File | Settings | File Templates.
  }

  override fun getCustomer(id: Long): Observable<Customer> {
    TODO(
        "not implemented"
    ) //To change body of created functions use File | Settings | File Templates.
  }

  override fun postTransaction(customer: Customer): Observable<Unit> {
    TODO(
        "not implemented"
    ) //To change body of created functions use File | Settings | File Templates.
  }

  override fun getRetailers(): Observable<List<Retailer>> {
    TODO(
        "not implemented"
    ) //To change body of created functions use File | Settings | File Templates.
  }

  override fun postRetailers(retailers: List<Retailer>): Observable<Unit> {
    TODO(
        "not implemented"
    ) //To change body of created functions use File | Settings | File Templates.
  }

  override fun getRetailer(id: Long): Observable<Retailer> {
    TODO(
        "not implemented"
    ) //To change body of created functions use File | Settings | File Templates.
  }

  override fun postRetailer(retailer: Retailer): Observable<Unit> {
    TODO(
        "not implemented"
    ) //To change body of created functions use File | Settings | File Templates.
  }
}

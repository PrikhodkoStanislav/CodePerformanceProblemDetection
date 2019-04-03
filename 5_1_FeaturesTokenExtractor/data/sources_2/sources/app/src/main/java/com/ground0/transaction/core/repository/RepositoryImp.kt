package com.ground0.transaction.core.repository

import android.util.Log
import com.ground0.model.Customer
import com.ground0.model.RetailTransaction
import com.ground0.model.Retailer
import com.ground0.transaction.core.repository.db.LocalStore
import com.ground0.transaction.core.repository.network.CloudStore
import io.reactivex.Observable

/**
 * Created by 00-00-00 on 08/05/18.
 */

object RepositoryImp : Repository {

  override fun getTransactions(): Observable<List<RetailTransaction>> {
    return CloudStore.getTransactions()
        .also {
          it.subscribe {
            LocalStore.postTransactions(it)
                .subscribe({ Log.d(RepositoryImp.javaClass.canonicalName, "DB write success") },
                    {
                      Log.d(RepositoryImp.javaClass.canonicalName, "DB write fail")
                    })
          }
        }
  }

  override fun getTransaction(id: Long): Observable<RetailTransaction> {
    TODO(
        "not implemented"
    ) //To change body of created functions use File | Settings | File Templates.
  }

  override fun postTransactions(retailTransactions: List<RetailTransaction>): Observable<Unit> {
    TODO(
        "not implemented"
    ) //To change body of created functions use File | Settings | File Templates.
  }

  override fun postTransaction(retailTransaction: RetailTransaction): Observable<Unit> {
    TODO(
        "not implemented"
    ) //To change body of created functions use File | Settings | File Templates.
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

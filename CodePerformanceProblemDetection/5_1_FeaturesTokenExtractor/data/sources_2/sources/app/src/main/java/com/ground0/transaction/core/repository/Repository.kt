package com.ground0.transaction.core.repository

import com.ground0.model.Customer
import com.ground0.model.RetailTransaction
import com.ground0.model.Retailer
import io.reactivex.Observable

/**
 * Created by 00-00-00 on 05/05/18.
 */

interface Repository {

  fun getTransactions(): Observable<List<RetailTransaction>>
  fun getTransaction(id: Long): Observable<RetailTransaction>
  fun postTransactions(retailTransactions: List<RetailTransaction>): Observable<Unit>
  fun postTransaction(retailTransaction: RetailTransaction): Observable<Unit>

  fun getCustomers(): Observable<List<Customer>>
  fun postCustomers(customers: List<Customer>): Observable<Unit>
  fun getCustomer(id: Long): Observable<Customer>
  fun postTransaction(customer: Customer): Observable<Unit>

  fun getRetailers(): Observable<List<Retailer>>
  fun postRetailers(retailers: List<Retailer>): Observable<Unit>
  fun getRetailer(id: Long): Observable<Retailer>
  fun postRetailer(retailer: Retailer): Observable<Unit>
}
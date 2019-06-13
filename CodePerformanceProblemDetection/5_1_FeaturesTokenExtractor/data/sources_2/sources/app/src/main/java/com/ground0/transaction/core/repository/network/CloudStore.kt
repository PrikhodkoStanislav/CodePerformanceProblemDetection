package com.ground0.transaction.core.repository.network

import com.google.gson.GsonBuilder
import com.ground0.model.Customer
import com.ground0.model.RetailTransaction
import com.ground0.model.Retailer
import com.ground0.transaction.BuildConfig
import com.ground0.transaction.core.repository.Repository
import com.ground0.transaction.core.repository.db.util.LocalDateTimeConverter
import com.ground0.transaction.core.repository.network.util.HttpStatusOperator
import io.reactivex.Observable
import io.reactivex.schedulers.Schedulers
import org.threeten.bp.LocalDateTime
import retrofit2.Response
import retrofit2.Retrofit
import retrofit2.adapter.rxjava2.RxJava2CallAdapterFactory
import retrofit2.converter.gson.GsonConverterFactory

/**
 * Created by 00-00-00 on 05/05/18.
 */

object CloudStore: Repository {

  private const val HOST = "${BuildConfig.HOST}${BuildConfig.API_VERSION}/"
  private lateinit var restImp: ApiStore

  fun init() {
    val retrofit = Retrofit.Builder()
        .addCallAdapterFactory(RxJava2CallAdapterFactory.create())
        .addConverterFactory(
            GsonConverterFactory.create(
                GsonBuilder().registerTypeAdapter(
                    LocalDateTime::class.java, LocalDateTimeConverter()
                ).create()
            )
        )
        .baseUrl(HOST)
        .build()

    restImp = retrofit.create(
        ApiStore::class.java
    )
  }

  fun getNon() =
    restImp.getNon().adapt()

  override fun getTransactions(): Observable<List<RetailTransaction>> =
    restImp.getTransactions().adapt()

  override fun getTransaction(id: Long): Observable<RetailTransaction> =
    restImp.getTransaction(id).adapt()

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

  private fun <T> Observable<Response<T>>.adapt(): Observable<T> =
    switchMapSingle(HttpStatusOperator()).subscribeOn(Schedulers.io())

}

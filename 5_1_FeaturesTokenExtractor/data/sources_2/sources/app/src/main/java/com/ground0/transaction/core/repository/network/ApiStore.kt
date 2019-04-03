package com.ground0.transaction.core.repository.network

import com.ground0.model.RetailTransaction
import io.reactivex.Flowable
import io.reactivex.Observable
import retrofit2.Response
import retrofit2.http.GET
import retrofit2.http.Query

/**
 * Created by 00-00-00 on 05/05/18.
 */

interface ApiStore {

  @GET("transactions")
  fun getTransactions(): Observable<Response<List<RetailTransaction>>>

  @GET("non_existant")
  fun getNon(): Observable<Response<Unit>>

  @GET("transaction/{transactionId}")
  fun getTransaction(@Query("transactionId") id: Long): Observable<Response<RetailTransaction>>

}
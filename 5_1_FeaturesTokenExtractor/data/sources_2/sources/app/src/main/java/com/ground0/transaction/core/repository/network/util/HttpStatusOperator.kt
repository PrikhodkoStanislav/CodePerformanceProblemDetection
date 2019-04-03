package com.ground0.transaction.core.repository.network.util

import io.reactivex.ObservableSource
import io.reactivex.SingleSource
import io.reactivex.functions.Function
import retrofit2.Response

/**
 * Created by 00-00-00 on 07/05/18.
 */

class HttpStatusOperator<T>: Function< Response<T>, SingleSource<T>> {
  override fun apply(t: Response<T>): SingleSource<T> {
    return SingleSource { observer ->
      if (t.isSuccessful) {
        observer.onSuccess(t.body())
      } else {
        observer.onError(Throwable("HTTP error"))
      }
    }
  }
}
package com.ground0.transaction.core.repository.network.util

import io.reactivex.SingleObserver
import io.reactivex.disposables.Disposable
import okhttp3.MediaType
import okhttp3.ResponseBody
import org.junit.Assert
import org.junit.Test
import retrofit2.Response

/**
 * Created by 00-00-00 on 08/05/18.
 */

class HttpStatusOperatorTest {

  @Test
  fun shouldCallOnErrorFor404() {
    val response: Response<Unit> =
      Response.error(404, ResponseBody.create(MediaType.parse("application/json"), ""))

    val statusOperator = HttpStatusOperator<Unit>()

    statusOperator.apply(response)
        .subscribe(object : SingleObserver<Unit> {
          override fun onSuccess(t: Unit) {
            assert(false, {"On Success was called"})
          }

          override fun onSubscribe(d: Disposable) {

          }

          override fun onError(e: Throwable) {
            assert(true, {"On Error was calledq"})
          }
        })
  }

  @Test
  fun shouldCallOnSuccessFor200() {
    val response: Response<Unit> =
      Response.success(Unit)
    val statusOperator = HttpStatusOperator<Unit>()
    statusOperator.apply(response)
        .subscribe(object : SingleObserver<Unit> {
          override fun onSuccess(t: Unit) {
            assert(true, {"On Success was called"})
          }

          override fun onSubscribe(d: Disposable) {

          }

          override fun onError(e: Throwable) {
            assert(false, {"On Error was called"})
          }
        })
  }
}


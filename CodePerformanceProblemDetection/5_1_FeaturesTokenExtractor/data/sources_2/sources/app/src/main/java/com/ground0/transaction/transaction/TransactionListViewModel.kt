package com.ground0.transaction.transaction

import android.arch.lifecycle.MutableLiveData
import android.arch.lifecycle.ViewModel
import android.util.Log
import com.ground0.model.RetailTransaction
import com.ground0.transaction.core.livedata.SingleLiveEvent
import com.ground0.transaction.core.repository.RepositoryImp
import io.reactivex.android.schedulers.AndroidSchedulers

/**
 * Created by 00-00-00 on 05/05/18.
 */

class TransactionListViewModel : ViewModel() {

  val
      transactions: MutableLiveData<List<RetailTransaction>> by lazy {
    loadTransactions()
    MutableLiveData<List<RetailTransaction>>()
  }
  val errorEvent = SingleLiveEvent<String>()

  private fun loadTransactions() {
    Log.d(this::class.java.name, "Loading transactions: ${System.currentTimeMillis()}")
    RepositoryImp.getTransactions()
        .observeOn(AndroidSchedulers.mainThread())
        .subscribe({ it ->
          Log.d(
              this@TransactionListViewModel.javaClass.canonicalName,
              "Rx observable triggered ${System.currentTimeMillis()}"
          )
          transactions.value = it
          errorEvent.value = "Yo, Shits done ${System.currentTimeMillis()}"
        }, {
          errorEvent.value = "Oh oh, dum dum ${it.message}"
        })
  }
}
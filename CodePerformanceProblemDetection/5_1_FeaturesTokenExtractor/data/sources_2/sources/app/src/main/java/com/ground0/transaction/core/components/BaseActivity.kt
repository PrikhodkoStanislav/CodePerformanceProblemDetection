package com.ground0.transaction.core.components

import android.arch.lifecycle.ViewModel
import android.arch.lifecycle.ViewModelProviders
import android.os.Bundle
import android.support.v7.app.AppCompatActivity

/**
 * Created by 00-00-00 on 10/05/18.
 */

abstract class BaseActivity<T : ViewModel> : AppCompatActivity() {

  protected lateinit var viewModel : T

  override fun onCreate(savedInstanceState: Bundle?) {
    super.onCreate(savedInstanceState)
  }

  protected fun initViewModel(clazz: Class<T>) {
    viewModel = ViewModelProviders.of(this).get(clazz)
  }
}

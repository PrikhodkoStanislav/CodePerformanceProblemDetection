package com.ground0.transaction

import android.arch.lifecycle.Observer
import android.arch.lifecycle.ViewModelProviders
import android.content.Intent
import android.os.Bundle
import android.support.design.widget.Snackbar
import android.support.v7.app.AppCompatActivity
import android.widget.TextView
import butterknife.ButterKnife
import butterknife.OnClick
import com.ground0.transaction.R.id
import com.ground0.transaction.transaction.TransactionListViewModel

class MainActivity : AppCompatActivity() {

  private lateinit var viewModel: TransactionListViewModel

  override fun onCreate(savedInstanceState: Bundle?) {
    super.onCreate(savedInstanceState)
    setContentView(R.layout.activity_main)
    ButterKnife.bind(this)
    viewModel = ViewModelProviders.of(this)
        .get(TransactionListViewModel::class.java)

    showTransactions()
    subscribeToMessages()
  }

  private fun showTransactions() {
    viewModel.transactions.observe(
        this@MainActivity,
        Observer {
          findViewById<TextView>(id.a_main_text).apply {
            text = it?.map { it.amount }
                ?.joinToString()
          }
        })
  }

  private fun subscribeToMessages() {
    viewModel.errorEvent.observe(
        this, Observer {
      it?.let {
        Snackbar.make(findViewById(R.id.a_main_container), it, Snackbar.LENGTH_SHORT)
            .show()
      }
    })
  }

  @OnClick(R.id.a_main_button)
  fun onButtonClick() {
    startActivity(Intent(this, Main2Activity::class.java))
  }
}

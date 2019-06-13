package com.ground0.transaction.transaction

import android.arch.lifecycle.Observer
import android.os.Bundle
import android.support.design.widget.Snackbar
import android.support.v7.widget.LinearLayoutManager
import android.support.v7.widget.RecyclerView
import butterknife.BindView
import butterknife.ButterKnife
import com.ground0.transaction.R
import com.ground0.transaction.core.components.BaseActivity

/**
 * Created by 00-00-00 on 10/05/18.
 */

class TransactionListActivity : BaseActivity<TransactionListViewModel>() {

  @BindView(R.id.a_transaction_list_recycler)
  lateinit var recyclerView: RecyclerView

  private var transactionListAdapter: TransactionListAdapter? = null

  override fun onCreate(savedInstanceState: Bundle?) {
    super.onCreate(savedInstanceState)

    setContentView(R.layout.activity_transaction_list)
    ButterKnife.bind(this)

    initViewModel(TransactionListViewModel::class.java)
    initRecyclerView()
    subscribeToTransactions()
    subscribeToError()
  }

  private fun initRecyclerView() {
    recyclerView.layoutManager = LinearLayoutManager(this, LinearLayoutManager.VERTICAL, false)
    recyclerView.adapter = transactionListAdapter
  }

  private fun subscribeToTransactions() {
    viewModel.transactions.observe(this, Observer {
      if (transactionListAdapter == null) {
        transactionListAdapter =
            TransactionListAdapter(it ?: listOf())
        recyclerView.adapter = transactionListAdapter
      }
      else {
        transactionListAdapter?.list = it ?: listOf()
        transactionListAdapter?.notifyDataSetChanged()
      }
    })
  }

  private fun subscribeToError() {
    viewModel.errorEvent.observe(this, Observer {
      Snackbar.make(
          findViewById(R.id.a_transaction_list_container), it ?: "Something went wrong",
          Snackbar.LENGTH_SHORT
      )
          .show()
    })
  }

}

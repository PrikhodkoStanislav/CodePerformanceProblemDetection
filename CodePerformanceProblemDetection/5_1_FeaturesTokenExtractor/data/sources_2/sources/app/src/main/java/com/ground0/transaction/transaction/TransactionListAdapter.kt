package com.ground0.transaction.transaction

import android.support.v7.widget.RecyclerView
import android.view.LayoutInflater
import android.view.View
import android.view.ViewGroup
import com.ground0.model.RetailTransaction
import com.ground0.transaction.R
import com.ground0.transaction.databinding.ItemTransactionBinding
import com.ground0.transaction.transaction.TransactionListAdapter.ViewHolder

/**
 * Created by 00-00-00 on 10/05/18.
 */

class TransactionListAdapter(var list: List<RetailTransaction>) : RecyclerView.Adapter<ViewHolder>() {

  val transactionListItemViewModelFactory = TransactionListItemViewModelFactory()
  override fun onCreateViewHolder(
    parent: ViewGroup,
    viewType: Int
  ): ViewHolder {
    val view = LayoutInflater.from(parent.context)
        .inflate(R.layout.item_transaction, parent, false)
    return ViewHolder(view)
  }

  override fun getItemCount(): Int = list.size

  override fun onBindViewHolder(
    holder: ViewHolder,
    position: Int
  ) {
    ItemTransactionBinding.bind(holder.itemView)
        .itemViewModel = transactionListItemViewModelFactory.createItemViewModel(list[position])
  }

  inner class ViewHolder(itemView: View) : RecyclerView.ViewHolder(itemView)
}
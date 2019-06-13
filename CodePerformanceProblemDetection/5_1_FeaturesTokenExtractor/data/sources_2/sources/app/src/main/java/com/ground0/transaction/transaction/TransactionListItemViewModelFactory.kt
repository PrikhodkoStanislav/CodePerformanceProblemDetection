package com.ground0.transaction.transaction

import com.ground0.model.RetailTransaction

/**
 * Created by 00-00-00 on 10/05/18.
 */

class TransactionListItemViewModelFactory {

  fun createItemViewModel(retailTransaction: RetailTransaction) : TransactionListItemViewModel =
    TransactionListItemViewModel(retailTransaction)

  inner class TransactionListItemViewModel internal constructor(val retailTransaction: RetailTransaction)
}
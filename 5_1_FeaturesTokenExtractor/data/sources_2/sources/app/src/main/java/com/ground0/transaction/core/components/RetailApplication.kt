package com.ground0.transaction.core.components

import android.app.Application
import com.ground0.transaction.core.repository.db.LocalStore
import com.ground0.transaction.core.repository.network.CloudStore
import com.jakewharton.threetenabp.AndroidThreeTen

/**
 * Created by 00-00-00 on 05/05/18.
 */


class RetailApplication: Application() {
  override fun onCreate() {
    super.onCreate()
    AndroidThreeTen.init(this)
    CloudStore.init()
    LocalStore.init(this)
  }
}
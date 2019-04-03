package com.ground0.transaction

import android.os.Bundle
import android.support.v7.app.AppCompatActivity
import android.widget.TextView
import android.widget.Toast
import com.ground0.transaction.core.repository.db.LocalStore
import io.reactivex.android.schedulers.AndroidSchedulers
import kotlinx.android.synthetic.main.activity_main2.toolbar

class Main2Activity : AppCompatActivity() {

  override fun onCreate(savedInstanceState: Bundle?) {
    super.onCreate(savedInstanceState)
    setContentView(R.layout.activity_main2)
    setSupportActionBar(toolbar)


    LocalStore.getTransactions()
        .observeOn(AndroidSchedulers.mainThread())
        .subscribe({
          findViewById<TextView>(R.id.a_main2_text).apply {
            text = it?.map { it.amount }
                ?.joinToString()
          }
        }, {
          Toast.makeText(this, "Error", Toast.LENGTH_SHORT)
              .show()
        })
  }

}

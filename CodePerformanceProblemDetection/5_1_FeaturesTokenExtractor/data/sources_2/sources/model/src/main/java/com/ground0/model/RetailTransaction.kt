package com.ground0.model

import android.arch.persistence.room.ColumnInfo
import android.arch.persistence.room.Entity
import android.arch.persistence.room.PrimaryKey
import com.google.gson.annotations.SerializedName
import org.threeten.bp.LocalDateTime

@Entity(tableName = "retail_transactions")
class RetailTransaction {

  @PrimaryKey
  var id: Long? = null

  @ColumnInfo(name = "amount")
  @SerializedName("amount_cents")
  var amount: Long? = null

  @ColumnInfo(name = "currency")
  @SerializedName("amount_currency")
  lateinit var currency: String

  @ColumnInfo(name = "created_at")
  @SerializedName("created_at")
  lateinit var createdAt: LocalDateTime

  @ColumnInfo(name = "updated_at")
  @SerializedName("updated_at")
  lateinit var updatedAt: LocalDateTime

  @ColumnInfo(name = "customer_id")
  @SerializedName("customer_id")
  var customerId: Long? = null

  @ColumnInfo(name = "retailer_id")
  @SerializedName("retailer_id")
  var retailerId: Long? = null
}

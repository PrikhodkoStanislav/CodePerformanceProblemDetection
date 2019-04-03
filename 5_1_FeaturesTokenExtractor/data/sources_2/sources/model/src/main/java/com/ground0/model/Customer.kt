package com.ground0.model

import com.google.gson.annotations.SerializedName
import java.util.Date

/**
 * Created by 00-00-00 on 04/05/18.
 */

open class Customer {
  @SerializedName("id")
  var id: Int? = null

  @SerializedName("name")
  var name: String? = null

  @SerializedName("email")
  var email: String? = null

  @SerializedName("phone")
  var phone: String? = null

  @SerializedName("created_at")
  lateinit var createdAt: Date

  @SerializedName("updated_at")
  lateinit var updatedAt: Date
}

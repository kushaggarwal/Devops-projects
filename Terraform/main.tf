resource "aws_dynamodb_table" "product_table" {

    name = "PRODUCT"
    billing_mode = "PAY_PER_REQUEST"
    hash_key = "product_id"


    attribute {
      name = "product_id"
      type = "S"
    }

    attribute {
      name = "category"
      type = "S"
    }

    attribute {
      name = "product_rating"
      type = "N"
    }

    global_secondary_index {
      name = "ProductCategoryRatingIndex"
      hash_key = "category"
      range_key = "product_rating"
      projection_type = "ALL"
    }
  
}

resource "aws_api_gateway_rest_api" "product_apigw" {
  name = "product_apigw"
  description = "Product API Gateway"
  endpoint_configuration {
    types = ["REGIONAL"]
  }
}
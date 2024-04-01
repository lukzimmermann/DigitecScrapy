import requests
import json
import time
import zlib
import os
from articleDetail import ArticleDetail

DETAIL_URL = 'https://www.digitec.ch/api/graphql/pdp-get-product-details'

class DigitecScrapy():
    def __init__(self) -> None:
        pass

    def get_article_details_as_json(self, article_number: int, print_out: bool = False, safe: bool = False, path: str = 'data') -> ArticleDetail:
        start = time.time()
        query = [{"operationName":"PDP_GET_PRODUCT_DETAILS","variables":{},"query":"query PDP_GET_PRODUCT_DETAILS($productId: Int!) {\n  productDetails: productDetailsV3(productId: $productId) {\n    mandatorSpecificData {\n      ...ProductMandatorSpecific\n      __typename\n    }\n    product {\n      ...ProductMandatorIndependent\n      description\n      __typename\n    }\n    offers {\n      ...ProductDetailsOffer\n      __typename\n    }\n    productDetails {\n      testReports {\n        id\n        averageGrade\n        numberOfTests\n        awardLabels\n        contents {\n          id\n          variantProductId\n          testerName\n          testerLogoLink\n          grade\n          testerGrade\n          awardLabel\n          awardLabels\n          magazineEdition\n          conclusion\n          pros\n          contras\n          isSingleTest\n          withoutPlacement\n          placement\n          testSeriesTitle\n          testSeriesTotalNumberOfProducts\n          testSeriesId\n          testDate\n          isMachineTranslation\n          __typename\n        }\n        __typename\n      }\n      ranking\n      specifications {\n        title\n        description\n        link\n        type\n        properties {\n          name\n          propertyId\n          propertyDefinitionId\n          description\n          descriptionLink\n          type\n          isSuggestedByUser\n          needsAssessment\n          editId\n          values {\n            value\n            description\n            descriptionLink\n            link\n            iconType\n            subValues {\n              value\n              link\n              __typename\n            }\n            __typename\n          }\n          __typename\n        }\n        __typename\n      }\n      repairabilityIndex {\n        score\n        __typename\n      }\n      images {\n        fileUrl\n        description\n        width\n        height\n        __typename\n      }\n      videos {\n        id\n        name\n        videoProvider\n        __typename\n      }\n      variants {\n        variantId\n        name\n        type\n        products {\n          productId\n          label\n          brandName\n          name\n          nameProperties\n          productTypeName\n          image {\n            url\n            height\n            width\n            __typename\n          }\n          __typename\n        }\n        __typename\n      }\n      marketingPageProductIds\n      incentives {\n        name\n        rewardName\n        description\n        link\n        validFrom\n        validTo\n        deadline\n        files {\n          name\n          languages\n          url\n          size\n          __typename\n        }\n        amount {\n          amount\n          currency\n          __typename\n        }\n        __typename\n      }\n      partnerServicesOverview {\n        titles\n        __typename\n      }\n      accessoryOfProducts {\n        productTypeName\n        productTypeId\n        productIds\n        __typename\n      }\n      accessories {\n        productTypeName\n        productTypeId\n        productIds\n        __typename\n      }\n      popularAccessoryProductIds\n      setProducts {\n        productId\n        quantity\n        __typename\n      }\n      buyInSetProductIds\n      termsAndConditions\n      redemptionInstructions\n      remarks {\n        title\n        description\n        __typename\n      }\n      canonicalUrl\n      youtubeVideos {\n        videoId\n        publishedAt\n        title\n        channelTitle\n        thumbnails {\n          default {\n            url\n            width\n            height\n            __typename\n          }\n          medium {\n            url\n            width\n            height\n            __typename\n          }\n          high {\n            url\n            width\n            height\n            __typename\n          }\n          __typename\n        }\n        __typename\n      }\n      seo {\n        book {\n          authors\n          isbn\n          __typename\n        }\n        fallbackPrice {\n          amountInclusive\n          amountExclusive\n          currency\n          __typename\n        }\n        __typename\n      }\n      prohibitedBlocks\n      packageSize\n      afterSalesScores {\n        return {\n          brandId\n          brandName\n          rank\n          score\n          isSignificant\n          __typename\n        }\n        warranty {\n          brandId\n          brandName\n          rank\n          score\n          isSignificant\n          __typename\n        }\n        throughputTime {\n          brandId\n          brandName\n          rank\n          score\n          isSignificant\n          __typename\n        }\n        warrantyCount\n        returnCount\n        throughputTimeCount\n        __typename\n      }\n      features\n      isSustainable\n      __typename\n    }\n    blockConfiguration {\n      expandedBlocks\n      __typename\n    }\n    redirectPortalId\n    __typename\n  }\n}\n\nfragment ProductMandatorSpecific on MandatorSpecificData {\n  isBestseller\n  isDeleted\n  showroomSites\n  sectorIds\n  hasVariants\n  __typename\n}\n\nfragment ProductMandatorIndependent on ProductV2 {\n  id\n  productId\n  name\n  nameProperties\n  productTypeId\n  productTypeName\n  brandId\n  brandName\n  averageRating\n  totalRatings\n  totalQuestions\n  isProductSet\n  images {\n    url\n    height\n    width\n    __typename\n  }\n  energyEfficiency {\n    energyEfficiencyColorType\n    energyEfficiencyLabelText\n    energyEfficiencyLabelSigns\n    energyEfficiencyImage {\n      url\n      height\n      width\n      __typename\n    }\n    __typename\n  }\n  seo {\n    seoProductTypeName\n    seoNameProperties\n    productGroups {\n      productGroup1\n      productGroup2\n      productGroup3\n      productGroup4\n      __typename\n    }\n    gtin\n    __typename\n  }\n  smallDimensions\n  basePrice {\n    priceFactor\n    value\n    __typename\n  }\n  productDataSheet {\n    name\n    languages\n    url\n    size\n    __typename\n  }\n  __typename\n}\n\nfragment ProductDetailsOffer on ProductDetailOffer {\n  id\n  productId\n  offerId\n  shopOfferId\n  price {\n    amountInclusive\n    amountExclusive\n    currency\n    __typename\n  }\n  deliveryOptions {\n    mail {\n      classification\n      futureReleaseDate\n      __typename\n    }\n    pickup {\n      siteId\n      classification\n      futureReleaseDate\n      __typename\n    }\n    detailsProvider {\n      productId\n      offerId\n      quantity\n      type\n      refurbishedId\n      resaleId\n      __typename\n    }\n    __typename\n  }\n  supplier {\n    name\n    countryIsoCode\n    countryName\n    customsType\n    link\n    __typename\n  }\n  label\n  labelType\n  type\n  volumeDiscountPrices {\n    minAmount\n    price {\n      amountInclusive\n      amountExclusive\n      currency\n      __typename\n    }\n    isDefault\n    __typename\n  }\n  salesInformation {\n    numberOfItems\n    numberOfItemsSold\n    isEndingSoon\n    __typename\n  }\n  incentiveText\n  isIncentiveCashback\n  isNew\n  isSalesPromotion\n  hideInProductDiscovery\n  canAddToBasket\n  hidePrice\n  insteadOfPrice {\n    type\n    price {\n      amountInclusive\n      amountExclusive\n      currency\n      __typename\n    }\n    referenceDate\n    __typename\n  }\n  minOrderQuantity\n  secondHandOfferInfo {\n    conditions {\n      name\n      value\n      description\n      __typename\n    }\n    generalCondition {\n      name\n      value\n      description\n      __typename\n    }\n    description\n    translatedDescription\n    sellerCustomerId\n    images {\n      fileUrl\n      description\n      width\n      height\n      __typename\n    }\n    __typename\n  }\n  returnText {\n    title\n    description\n    type\n    __typename\n  }\n  insuranceOverviews {\n    title\n    __typename\n  }\n  warrantyDescriptions {\n    title\n    description\n    tooltip\n    type\n    __typename\n  }\n  digitecConnect {\n    months\n    value\n    type\n    __typename\n  }\n  specifications {\n    title\n    description\n    link\n    type\n    properties {\n      name\n      propertyId\n      description\n      descriptionLink\n      type\n      isSuggestedByUser\n      needsAssessment\n      values {\n        value\n        description\n        descriptionLink\n        link\n        propertyDefinitionOptionId\n        iconType\n        subValues {\n          value\n          link\n          __typename\n        }\n        __typename\n      }\n      __typename\n    }\n    __typename\n  }\n  priceWithoutCustomerGroup {\n    amountInclusive\n    amountExclusive\n    currency\n    __typename\n  }\n  __typename\n}"}]
        query[0]['variables'] = {'productId': article_number}

        request_body = json.dumps(query)
        content_length = len(request_body)

        headers = {
            'Content-Type': 'application/json',
            'Content-Length': str(content_length),
            'User-Agent': 'DiniMueter/2.0.0',
            'Accept-Encoding': '*/*',
            'Host': 'www.digitec.ch'
        }

        response = requests.post(DETAIL_URL, data=request_body, headers=headers)

        article = ArticleDetail(response.json())

        if safe: self.__safe_json(response.json(), path, article_number)
        if print_out: self.__print_out(article)
        
        print(f'Time: {(time.time()-start)*1000}')

        return article

    def __safe_json(self, json_data, path, article_number):
        if not os.path.exists(path):
            os.makedirs(path)

        json_string = json.dumps(json_data)
        compressed_data = zlib.compress(json_string.encode())
        with open(f'data/{article_number}_detail.zio', 'wb') as file:
            file.write(compressed_data)

        with open(f'data/{article_number}_detail.json', 'wb') as file:
            file.write(json_string.encode('utf-8'))

    def __print_out(self, article: ArticleDetail):
        text = "======================================================================\n"
        text += f'Number:          {article.number}\n'
        text += f'Name:            {article.name}\n'
        text += f'Brand:           {article.brand_name}\n'
        text += f'Category         {article.product_type}\n'
        text += f'Rating:          {article.average_rating}\n'
        text += f'Total Rating:    {article.total_ratings}\n'
        text += f'Total Questions: {article.total_questions}\n'
        text += f'Price:'
        first_row = True
        for supplier in article.suppliers:
            if first_row:
                text += f'           {supplier.name}: {supplier.price}{supplier.currency}\n'
                first_row = False
            else:
                text += f'                 {supplier.name}: {supplier.price}{supplier.currency}\n'
        
        text += f'Specification:'
        first_row = True
        for spec in article.specification:
            if first_row:
                text += f'   {spec.name}: {spec.value}\n'
                first_row = False
            else:
                text += f'                 {spec.name}: {spec.value}\n'

        text += "======================================================================\n"


        print(f'{text}')

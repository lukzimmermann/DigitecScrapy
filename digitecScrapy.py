import requests
import json
import zlib
import os
from articleDetail import ArticleDetail, DeliveryOption

DETAIL_URL = 'https://www.digitec.ch/api/graphql/pdp-get-product-details'

class DigitecScrapy():
    def __init__(self) -> None:
        pass

    def get_article_details(self, article_number: int, print_out: bool = False, safe_zio: bool = False, path: str = 'data') -> ArticleDetail:
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

        if safe_zio: self.__safe_zio(response.json(), path, article_number)
        if print_out: self.__print_out(article)

        return article

    def __safe_zio(self, json_data, path, article_number):
        if not os.path.exists(path):
            os.makedirs(path)

        json_string = json.dumps(json_data)
        compressed_data = zlib.compress(json_string.encode())
        with open(f'data/{article_number}_detail.zio', 'wb') as file:
            file.write(compressed_data)

    def __print_out(self, article: ArticleDetail):
        first_column, second_column = self._get_column_size(article)
        text =  f"╔═{'═' * (first_column + second_column)}═╗\n"
        text += f'║ {"Article number:":<{first_column}}{article.number:<{second_column}} ║\n'
        text += f'║ {"Name:":<{first_column}}{article.name:<{second_column}} ║\n'
        text += f'║ {"Brand:":<{first_column}}{article.brand_name:<{second_column}} ║\n'
        text += f'║ {"Category":<{first_column}}{article.product_type:<{second_column}} ║\n'
        text += f'║ {"Rating:":<{first_column}}{article.average_rating:<{second_column}} ║\n'
        text += f'║ {"Total Rating:":<{first_column}}{article.total_ratings:<{second_column}} ║\n'
        text += f'║ {"Total Questions:":<{first_column}}{article.total_questions:<{second_column}} ║\n'
        
        text += f'║ {"":<{first_column+second_column}} ║\n'
        text += f'║ {"":<{first_column+second_column}} ║\n'
        text += f'║ {"Prices":<{first_column+second_column}} ║\n'
        text +=  f"║ {'-' * (first_column + second_column)} ║\n"
        digitec_availability: DeliveryOption = None
        for supplier in article.suppliers:
            if supplier.name == 'Galaxus': digitec_availability = supplier.delivery_options
            text += f'║ {supplier.name:<{first_column}}{(str(str(supplier.price) +" "+ supplier.currency)):<{second_column}} ║\n'

        text += f'║ {"":<{first_column+second_column}} ║\n'
        text += f'║ {"":<{first_column+second_column}} ║\n'
        text += f'║ {"Availability Digitec":<{first_column+second_column}} ║\n'
        text +=  f"║ {'-' * (first_column + second_column)} ║\n"
        text += f'║ {"Mail:":<{first_column}}{digitec_availability.mail.lower():<{second_column}} ║\n'
        for key, value in digitec_availability.shops.items():
            text += f'║ {str(key+":"):<{first_column}}{value.lower():<{second_column}} ║\n'
            
        for specification_group in article.specification:
            text += f'║ {"":<{first_column+second_column}} ║\n'
            text += f'║ {"":<{first_column+second_column}} ║\n'
            text += f'║ {specification_group.title:<{first_column+second_column}} ║\n'
            text +=  f"║ {'-' * (first_column + second_column)} ║\n"

            for specification in specification_group.specifications:
                spec_text = f'{str(specification.name + ":"):<{first_column-1}} {specification.value:<{second_column}}'
                text += f'║ {spec_text:<{first_column+second_column}} ║\n'

        text += f"╚═{'═' * (first_column + second_column)}═╝\n"


        print(f'{text}')

    def _get_column_size(self, article: ArticleDetail):
        first_column = 28
        second_column = 40

        for specification_group in article.specification:
            for specification in specification_group.specifications:
                if len(specification.name) > first_column: first_column = len(specification.name)+3
                if len(specification.value) > second_column: second_column = len(specification.value)+3
        return first_column, second_column

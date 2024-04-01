import json

class ArticleDetail():
    def __init__(self, data_json) -> None:

        data = data_json[0]['data']['productDetails']
        self.number: int = data['product']['productId']
        self.name: str = data['product']['name']
        self.product_type_id: int = data['product']['productTypeId']
        self.product_type: str = data['product']['productTypeName']
        self.brand_id: int = data['product']['brandId']
        self.brand_name: int = data['product']['brandName']
        self.average_rating: float = data['product']['averageRating']
        self.total_ratings: int = data['product']['totalRatings']
        self.total_questions: int = data['product']['totalQuestions']
        self.description: str = data['product']['description']
        self.small_dimension: bool = data['product']['smallDimensions']
        self.is_bestseller: bool = data['mandatorSpecificData']['isBestseller']
        self.is_deleted: bool = data['mandatorSpecificData']['isDeleted']
        self.images: list[Image] = self.__get_images(data['product']['images'])
        self.suppliers: list[Supplier] = self.__get_supplier(data['offers'])

    def __get_images(self, image_data_json):
        images: list[Image] = []
        for i in range(len(image_data_json)):
            images.append(Image(image_data_json[i]))
        return images
    
    def __get_supplier(self, supplier_data_json):
        suppliers: list[Supplier] = []
        for i in range(len(supplier_data_json)):
            suppliers.append(Supplier(supplier_data_json[i]))
        return suppliers

    def __repr__(self) -> str:
        return f'{self.number:8}  {self.name:40}  {self.product_type:20}'

class Image():
    def __init__(self, data) -> None:
        self.url = data['url']
        self.height = data['height']
        self.width = data['width']
    
    def __repr__(self) -> str:
        return f'{self.width}x{self.width}  {self.url}'

class Supplier():
    def __init__(self, data) -> None:
        print(data)
        if data['supplier'] is not None:
            self.name: str = data['supplier']['name']
        else:
            self.name = 'Unknown'
        self.price: float = data['price']['amountInclusive']
        self.currency: str = data['price']['currency']
        self.is_new: bool = data['isNew']
        self.is_promotion: bool = data['isSalesPromotion']
        self.is_hidden: bool = data['hideInProductDiscovery']
        self.is_price_hidden: bool = data['hidePrice']
        self.is_order_possible: bool = data['canAddToBasket']
        self.delivery_options: DeliveryOption = DeliveryOption(data['deliveryOptions'])

    def __repr__(self) -> str:
        return f'{self.price}{self.currency} @ {self.name}'

class DeliveryOption():
    def __init__(self, data) -> None:
        self.mail: str = data['mail']['classification']
        self.shops: dict[str, str] = self.__get_shops_status(data)

    def __get_shops_status(self, data):
        shop_status = {}
        for i in range(len(data['pickup'])):
            if data['pickup'][i]['siteId'] == 246938:
                shop_status['Zuerich'] = data['pickup'][i]['classification']
            elif data['pickup'][i]['siteId'] == 246965:
                shop_status['Lausanne'] = data['pickup'][i]['classification']
            elif data['pickup'][i]['siteId'] == 246967:
                shop_status['Basel'] = data['pickup'][i]['classification']
            elif data['pickup'][i]['siteId'] == 246968:
                shop_status['Kriens'] = data['pickup'][i]['classification']
            elif data['pickup'][i]['siteId'] == 246969:
                shop_status['Winterthur'] = data['pickup'][i]['classification']
            elif data['pickup'][i]['siteId'] == 246970:
                shop_status['Bern'] = data['pickup'][i]['classification']
            elif data['pickup'][i]['siteId'] == 246971:
                shop_status['Dietikon'] = data['pickup'][i]['classification']
            elif data['pickup'][i]['siteId'] == 246974:
                shop_status['St. Gallen'] = data['pickup'][i]['classification']
            elif data['pickup'][i]['siteId'] == 246975:
                shop_status['Genf'] = data['pickup'][i]['classification']
            elif data['pickup'][i]['siteId'] == 246977:
                shop_status['Wohlen'] = data['pickup'][i]['classification']
        return shop_status
    
    def __repr__(self) -> str:
        shop_info = ''
        for key, value in self.shops.items():
            shop_info += f'\n{key}: {value}'
        return f'Mail: {self.mail}{shop_info}'
import scrapy
import json
class MineSpider(scrapy.Spider):
    name = "mine"
    headers = {
        "Accept": "*/*",
        "Accept-Encoding": "gzip, deflate, br",
        "Accept-Language": "en-US,en;q=0.9",
        "Content-Length": "354",
        "Content-Type": "text/plain",
        "Origin": "https://www.ashleyfurniture.com",
        "Sec-Ch-Ua": 'Not.A/Brand";v="8", "Chromium";v="114", "Google Chrome";v="114',
        "Sec-Ch-Ua-Mobile": "?0",
        "Sec-Ch-Ua-Platform": "Windows",
        "Sec-Fetch-Dest": "empty",
        "Sec-Fetch-Mode": "cors",
        "Sec-Fetch-Site": "cross-site",
        "User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/114.0.0.0 Safari/537.36"

    }

    start_urls = [
        'https://www.ashleyfurniture.com/c/furniture/living-room/sofas/',
        'https://www.ashleyfurniture.com/c/furniture/living-room/loveseats/',
        'https://www.ashleyfurniture.com/c/furniture/living-room/sectional-sofas/',
        'https://www.ashleyfurniture.com/c/furniture/living-room/sleeper-sofas/',
        'https://www.ashleyfurniture.com/c/furniture/sets/living-room-sets/',
        'https://www.ashleyfurniture.com/c/furniture/living-room/reclining-furniture/',
        'https://www.ashleyfurniture.com/c/furniture/home-theater/seating/',
        'https://www.ashleyfurniture.com/c/furniture/living-room/living-room-chairs/',
        'https://www.ashleyfurniture.com/c/furniture/living-room/recliners/',
        'https://www.ashleyfurniture.com/c/furniture/living-room/ottomans/',
        'https://www.ashleyfurniture.com/c/furniture/living-room/coffee-tables/',
        'https://www.ashleyfurniture.com/c/furniture/living-room/end-and-side-tables/',
        'https://www.ashleyfurniture.com/c/furniture/living-room/tv-stands/',
        'https://www.ashleyfurniture.com/c/furniture/living-room/storage/accent-cabinets/',
        'https://www.ashleyfurniture.com/c/furniture/home-theater/shop-all/',
        'https://www.ashleyfurniture.com/c/furniture/bedroom/beds/',
        'https://www.ashleyfurniture.com/c/furniture/sets/bedroom-sets/',
        'https://www.ashleyfurniture.com/c/furniture/bedroom/headboards/',
        'https://www.ashleyfurniture.com/c/furniture/bedroom/dressers/',
        'https://www.ashleyfurniture.com/c/furniture/bedroom/dressers/mirrored/',
        'https://www.ashleyfurniture.com/c/furniture/bedroom/nightstands/',
        'https://www.ashleyfurniture.com/c/furniture/sets/dining-room-sets/',
        'https://www.ashleyfurniture.com/c/furniture/kitchen-and-dining-room/dining-room-tables/',
        'https://www.ashleyfurniture.com/c/furniture/kitchen-and-dining-room/chairs/',
        'https://www.ashleyfurniture.com/c/furniture/kitchen-and-dining-room/dining-benches/',
        'https://www.ashleyfurniture.com/c/furniture/kitchen-and-dining-room/bar-stools/',
        'https://www.ashleyfurniture.com/c/furniture/kitchen-and-dining-room/dining-storage/',
        'https://www.ashleyfurniture.com/c/furniture/home-office/desks/',
        'https://www.ashleyfurniture.com/c/furniture/home-office/bookcases/',
        'https://www.ashleyfurniture.com/c/furniture/home-office/office-chairs/',
        'https://www.ashleyfurniture.com/c/furniture/sets/home-office-sets/',
        'https://www.ashleyfurniture.com/c/furniture/home-office/office-storage/',
        'https://www.ashleyfurniture.com/c/furniture/gaming/',
        'https://www.ashleyfurniture.com/c/furniture/living-room/living-room-chairs/',
        'https://www.ashleyfurniture.com/c/furniture/living-room/storage/accent-cabinets/',
        'https://www.ashleyfurniture.com/c/furniture/benches/',
        'https://www.ashleyfurniture.com/c/furniture/living-room/ottomans/',
        'https://www.ashleyfurniture.com/c/furniture/living-room/console-tables/',
        'https://www.ashleyfurniture.com/c/furniture/living-room/occasional-tables/',
        'https://www.ashleyfurniture.com/c/furniture/living-room/end-and-side-tables/',
        'https://www.ashleyfurniture.com/c/furniture/living-room/coffee-tables/',
        'https://www.ashleyfurniture.com/c/furniture/kitchen-and-dining-room/bar/',
        'https://www.ashleyfurniture.com/c/furniture/living-room/console-tables/',
        'https://www.ashleyfurniture.com/c/entryway/benches/',
        'https://www.ashleyfurniture.com/c/furniture/living-room/storage/accent-cabinets/',
        'https://www.ashleyfurniture.com/c/home-decor/home-accents/artificial-plants/',
        'https://www.ashleyfurniture.com/c/home-decor/mirrors/wall-mirrors/',
        'https://www.ashleyfurniture.com/c/rugs/all/runner_rugs/',
        'https://www.ashleyfurniture.com/c/furniture/sets/',
        'https://www.ashleyfurniture.com/c/outdoor/patio-furniture/seating/sofa-and-loveseats/',
        'https://www.ashleyfurniture.com/c/outdoor/patio-furniture/seating/sectionals/',
        'https://www.ashleyfurniture.com/c/outdoor/outdoor-sets/conversation-sets/',
        'https://www.ashleyfurniture.com/c/outdoor/outdoor-sets/seating-sets/',
        'https://www.ashleyfurniture.com/c/outdoor/patio-furniture/seating/lounge-chairs/',
        'https://www.ashleyfurniture.com/c/outdoor/outdoor-seating/',
        'https://www.ashleyfurniture.com/c/outdoor/outdoor-sets/',
        'https://www.ashleyfurniture.com/c/outdoor/outdoor-dining/',
        'https://www.ashleyfurniture.com/c/outdoor/bar-furniture/',
        'https://www.ashleyfurniture.com/c/outdoor/outdoor-accessories/fire-pits/',
        'https://www.ashleyfurniture.com/c/outdoor/patio-accessories/',
        'https://www.ashleyfurniture.com/c/kids/beds/',
        'https://www.ashleyfurniture.com/c/kids/bunk-beds/',
        'https://www.ashleyfurniture.com/c/kids/loft-beds/',
        'https://www.ashleyfurniture.com/c/kids/headboards/',
        'https://www.ashleyfurniture.com/c/kids/bedroom-sets/',
        'https://www.ashleyfurniture.com/c/kids/dressers/',
        'https://www.ashleyfurniture.com/c/kids/furniture/kids-dressers/kids-dressers-and-mirrors/',
        'https://www.ashleyfurniture.com/c/kids/nightstands/',
        'https://www.ashleyfurniture.com/c/kids/storage/',
        'https://www.ashleyfurniture.com/c/kids/seating/',
        'https://www.ashleyfurniture.com/c/kids/kids-desks/',
        'https://www.ashleyfurniture.com/c/kids/tables-and-chairs/',
        'https://www.ashleyfurniture.com/c/kids/playroom/',
        'https://www.ashleyfurniture.com/c/baby-and-toddler/nursery/cribs/',
        'https://www.ashleyfurniture.com/c/baby-and-toddler/nursery/rocking-chairs-and-gliders/',
        'https://www.ashleyfurniture.com/c/baby-and-toddler/nursery/storage/',
        'https://www.ashleyfurniture.com/c/baby-and-toddler/nursery/collections/',
        'https://www.ashleyfurniture.com/c/baby-and-toddler/mattresses/',
        'https://www.ashleyfurniture.com/c/baby-and-toddler/nursery/bassinets/',
        'https://www.ashleyfurniture.com/c/baby-and-toddler/nursery/changing-tables-and-dressers/',
        'https://www.ashleyfurniture.com/c/baby-and-toddler/baby-gear/baby-strollers/',
        'https://www.ashleyfurniture.com/c/baby-and-toddler/toddler-beds/',
        'https://www.ashleyfurniture.com/c/baby-and-toddler/seating/',
        'https://www.ashleyfurniture.com/c/baby-and-toddler/bedding/',
        'https://www.ashleyfurniture.com/c/baby-and-toddler/nursery/side-tables-and-nightstands/',
        'https://www.ashleyfurniture.com/c/storage/cubes/',
        'https://www.ashleyfurniture.com/c/storage/jewelry/',
        'https://www.ashleyfurniture.com/c/storage/furniture-and-accents/',
        'https://www.ashleyfurniture.com/c/furniture/storage/closet-systems/',
        'https://www.ashleyfurniture.com/c/furniture/storage/free-standing-closets/',
        'https://www.ashleyfurniture.com/c/furniture/storage/closet/towers/',
        'https://www.ashleyfurniture.com/c/storage/boxes-and-totes/',
        'https://www.ashleyfurniture.com/c/storage/containers-and-drawers/',
        'https://www.ashleyfurniture.com/c/furniture/storage/shoe-racks/',
        'https://www.ashleyfurniture.com/c/home-decor/wall-decor/shelves/',
        'https://www.ashleyfurniture.com/c/storage/shelves/',
        'https://www.ashleyfurniture.com/c/furniture/home-office/bookcases/',
        'https://www.ashleyfurniture.com/c/bathroom/vanities/',
        'https://www.ashleyfurniture.com/c/bathroom/storage/',
        'https://www.ashleyfurniture.com/c/bathroom/storage/trash-cans-laundry-hampers/',
        'https://www.ashleyfurniture.com/c/bathroom/towel-racks/?start=0&sz=16',
        'https://www.ashleyfurniture.com/c/home-decor/home-accents/artificial-plants/',
        'https://www.ashleyfurniture.com/c/home-decor/home-accents/decorative-objects/',
        'https://www.ashleyfurniture.com/c/home-decor/home-accents/decorative-vases/',
        'https://www.ashleyfurniture.com/c/home-decor/home-accents/candle-holders/',
        'https://www.ashleyfurniture.com/c/home-decor/sculptures/',
        'https://www.ashleyfurniture.com/c/home-decor/picture-frames/',
        'https://www.ashleyfurniture.com/c/home-decor/home-accents/storage-baskets/',
        'https://www.ashleyfurniture.com/c/home-decor/wall-decor/',
        'https://www.ashleyfurniture.com/c/lighting/all/',
        'https://www.ashleyfurniture.com/c/rugs/area-rugs/',
        'https://www.ashleyfurniture.com/c/home-decor/textiles/',
        'https://www.ashleyfurniture.com/c/home-decor/poufs/',
        'https://www.ashleyfurniture.com/c/lighting/all/',
    ]

    def start_requests(self):
        for url in self.start_urls:
            yield scrapy.Request(url=url, callback=self.parse, meta={'render': True})

    def parse(self, response):
        products = response.xpath("//div[@class='product-name']/a")
        for product in products:
            product_link = product.xpath("./@href").get()

            yield scrapy.Request(product_link, callback=self.info_scraper,
                                 headers=self.headers)

        next_page = response.xpath("//*[@id='primary']/div[3]/div/ul/li[6]/a/@href").get()
        if next_page:
            yield scrapy.Request(next_page, callback=self.parse, headers=self.headers)


    def info_scraper(self, response):
        room_category = response.xpath("//ol[@class='breadcrumb']/li[last()-2]/a/text()").get()
        if room_category:
            room_category = room_category.strip()
        target_type = 'Product'
        script_tags = response.xpath('//script[@type="application/ld+json"]/text()').getall()

        json_data = None
        for script_tag in script_tags:
            try:
                data = json.loads(script_tag)
                if data.get('@type') == target_type:
                    json_data = data
                    break
            except json.JSONDecodeError as err:
                self.logger.error(f"JSON decoding error: {err}")
                self.logger.error(f"Failed to decode the following response: {script_tag}")

        if json_data:
            Retailer = "ashleyfurniture.com"
            category = response.xpath("(//a[@class='breadcrumb-element'])[last()]/text()").get()
            if category is not None:
                category = category.strip()
            else:
                pass
            product_color = response.xpath("//span[@class='selected-variant']/text()").get()
            if product_color is not None:
                product_color = product_color.strip()
            else:
                pass

            title = json_data['name']
            url = json_data['url']
            images = json_data['image']
            description = json_data['description']
            brand = json_data['brand']['name']
            if brand is None:
                brand = "Signature Design by Ashley®"
            sku = json_data['sku']
            price = json_data['offers']['price']
            yield {
                "Title": title,
                "Description": description,
                "Room Categories": room_category,
                "Item Categories": category,
                "Price": price,
                "Sku": sku,
                "Url": url,
                "Images": images,
                "Colors": product_color,
                "Brand": brand,
                "Retailer": Retailer
            }



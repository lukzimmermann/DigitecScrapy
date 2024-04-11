from src.model.articleDetail import Article

class Status():
    def __init__(self, job_id: str, 
                 start: int, end: int, 
                 current_article: int, 
                 number_of_article: int, 
                 last_articles: list[Article]) -> None:
        self.job_id: str = job_id
        self.start: int = start
        self.end: int = end
        self.article_range: str = f'{start} - {end}'
        self.current_article: int = current_article
        self.progress: str = self.__get_progress(start, end, current_article)
        self.number_of_article: int = number_of_article
        self.last_articles: list[Article] = last_articles

    def __get_progress(self, start: int, end: int, current_article: int):
        return f'{(current_article-start)/(end-start)*100:.1f}%'


class StatusPrinter():
    def __init__(self, column1_width:int = 30, column2_width:int = 30,  column3_width:int = 30) -> None:
        self.column1_width = column1_width
        self.column2_width = column2_width
        self.column3_width = column3_width
        self.width = column1_width + column2_width + column3_width

    def print_status(self, status: Status, number_of_article: int):
        progress_text = "Progress:"
        article_range_text = "Article number range:"
        job_id_text = "Job-ID:"
        current_article_number_text = "Current article number:"
        number_of_articles_found_text = 'Number of articles found:'

        column1_name = "Category"
        column2_name = "Article number"
        column3_name = "Article name"

        print(f"╔═{'═' * (self.width)}═╗")
        print(f'║ {job_id_text:<{self.column1_width}}{status.job_id:<{self.column2_width+self.column3_width}} ║')
        print(f'║ {article_range_text:<{self.column1_width}}{status.article_range:<{self.column2_width+self.column3_width}} ║')
        print(f'║ {current_article_number_text:<{self.column1_width}}{status.current_article:<{self.column2_width+self.column3_width}} ║')
        print(f'║ {progress_text:<{self.column1_width}}{status.progress:<{self.column2_width+self.column3_width}} ║')
        print(f'║ {number_of_articles_found_text:<{self.column1_width}}{status.number_of_article:<{self.column2_width+self.column3_width}} ║')
        print(f"║ {' ' * (self.width)} ║")
        print(f'║ {column1_name:<{self.column1_width}}{column2_name:{self.column2_width}}{column3_name:{self.column3_width}} ║')
        print(f"║ {'-' * (self.width)} ║")

        if number_of_article > len(status.last_articles):
            number_of_article = len(status.last_articles)-1

        #for i in range(number_of_article):
        for i in range(len(status.last_articles)-number_of_article, len(status.last_articles)):
            article = status.last_articles[i]
            if len(str(article.product_type)) > self.column1_width: number = str(article.product_type)[0:self.column1_width-4]
            else: number = article.product_type

            if len(str(article.number)) > self.column2_width: brand = str(article.number)[0:self.column2_width-4]
            else: brand = article.number

            if len(str({article.brand_name + " - " + article.name})) > self.column3_width: name = str(article.brand_name + " - " + article.name)[0:self.column3_width-4]
            else: name = f'{article.brand_name + " - " + article.name}'


            print(f'║ {number:<{self.column1_width}}{brand:<{self.column2_width}}{name:<{self.column3_width}} ║')

        print(f"╚═{'═' * (self.width)}═╝")
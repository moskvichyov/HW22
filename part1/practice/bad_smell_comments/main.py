# В данном коде все прокомментировано как надо,
# но слишком избыточно.
# Избавьтесь от комментариев, изменив имена переменных, 
# чтобы было понятно, за что эти переменные отвечают 
# и что происходит и без комментариев


class Unit:

    def move(self, field, x_param, y_param, direct, is_fly: bool, is_crawl: bool, speed: int=1):

        if is_fly and is_crawl:
            raise ValueError('Рожденный ползать летать не должен!')
        if is_fly:
            speed *= 1.2
            if direct == 'UP':
                new_y = y_param + speed
                new_x = x_param
            elif direct == 'DOWN':
                new_y = y_param - speed
                new_x = x_param
            elif direct == 'LEFT':
                new_y = y_param
                new_x = x_param - speed
            elif direct == 'RIGHT':
                new_y = y_param
                new_x = x_param + speed
        if is_crawl:
            speed *= 0.5
            if direct == 'UP':
                new_y = y_param + speed
                new_x = x_param
            elif direct == 'DOWN':
                new_y = y_param - speed
                new_x = x_param
            elif direct == 'LEFT':
                new_y = y_param
                new_x = x_param - speed
            elif direct == 'RIGHT':
                new_y = y_param
                new_x = x_param + speed

            field.set_unit(x=new_x, y=new_y, unit=self)



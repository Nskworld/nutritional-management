from django.db import models

class Food(models.Model):
    """食品モデル

        ▼項目一覧
        id: 食品ID
        name: 食品名
        food_category_id: 食品カテゴリID
        calorie: カロリー(kcal)
        protein: たんぱく質(g)
        fat: 脂質(g)
        carbohydrate: 炭水化物(g)
        delete_flg: 削除済みフラグ
        created_datetime: 作成日
        updated_datetime: 更新日

    """
    id = models.AutoField(primary_key=True)
    name = models.CharField(max_length=255, blank=True, null=True)
    food_category_id = models.IntegerField(blank=False, null=False, default=0)
    calorie = models.FloatField(blank=True, null=True)
    protein = models.FloatField(blank=True, null=True)
    fat = models.FloatField(blank=True, null=True)
    carbohydrate = models.FloatField(blank=True, null=True)
    delete_flg = models.BooleanField(default=False)
    created_datetime = models.DateTimeField(auto_now_add=True)
    updated_datetime = models.DateTimeField(auto_now=True)

    class Meta:
        db_table = 'food'

    def __str__(self):
        return self.name


class FoodCategory(models.Model):
    """食品カテゴリモデル

        ▼項目一覧
        id: 食品ID
        category: 食品カテゴリ
            0: 未設定
            1: 主食
            2: 主菜
            3: 副菜
            4: その他
        delete_flg: 削除済みフラグ
        created_datetime: 作成日
        updated_datetime: 更新日

    """
    id = models.AutoField(primary_key=True)
    category = models.IntegerField(blank=False, null=False, default=0)
    delete_flg = models.BooleanField(default=False)
    created_datetime = models.DateTimeField(auto_now_add=True)
    updated_datetime = models.DateTimeField(auto_now=True)

    class Meta:
        db_table = 'food_category'

    def __str__(self):
        return self.name
# vk-analytics

### Как установить

Python3 должен быть уже установлен. 
Затем используйте `pip` (или `pip3`, есть есть конфликт с Python2) для установки зависимостей:
```
pip install -r requirements.txt
```


### Как авторизоваться

   
1. Создайте [приложение Вконтакте][3]
   * В качестве типа приложения следует указать __standalone__
   * Получите __client_id__ созданного приложения
       * Если нажать на кнопку "Редактировать" для нового приложения, в адресной строке вы увидите его __client_id__.
   * Получите личный ключ (__access_token__)
       * в строке браузера сделайте запрос (вместо CLIENT_ID вставьте ваш __client_id__) :  
       `https://oauth.vk.com/authorize?client_id=CLIENT_ID&display=page&response_type=token&v=5.95&scope=photos,groups,wall,offline` 
       * При получении ключа вы увидите [такую страницу][2]. Список разрешений должен быть как на скриншоте.
         
2. Создайте в корневой папке файл ```.env``` и пропишите в нем свои данные следующим образом:  
     ```
     access_token=dhs1sdgd2ghjf3fhjf4fdjg5fghfdg6dh
     ``` 
   
[2]: https://dvmn.org/media/filer_public/0b/cd/0bcd3fe4-8eb9-404c-9684-e34ec03662d7/test.png "Скриншот."   
[3]: https://vk.com/apps?act=manage "Мои приложения."
# KYJstream

This project was generated with [Angular CLI](https://github.com/angular/angular-cli) version 11.0.2.

## Development server

Run `ng serve` for a dev server. Navigate to `http://localhost:4200/`. The app will automatically reload if you change any of the source files.

## Code scaffolding

Run `ng generate component component-name` to generate a new component. You can also use `ng generate directive|pipe|service|class|guard|interface|enum|module`.

## Build

Run `ng build` to build the project. The build artifacts will be stored in the `dist/` directory. Use the `--prod` flag for a production build.

## Running unit tests

Run `ng test` to execute the unit tests via [Karma](https://karma-runner.github.io).

## Running end-to-end tests

Run `ng e2e` to execute the end-to-end tests via [Protractor](http://www.protractortest.org/).

## Further help

To get more help on the Angular CLI use `ng help` or go check out the [Angular CLI Overview and Command Reference](https://angular.io/cli) page.

# 前端新建專案:

  ## 下載版本為:14.15.0的node.JS :  

  ## 安裝Angular CLI:
    npm install -g @angular/cli
    -g表示安裝在global

  ## 補其他所需檔案:
    npm install 
    
  ## 啟SERVE，改用0.0.0.0IP:
    ng serve --host 0.0.0.0

# 前端新建專案(Docker):
  ## 建立環境:  
  ```
  docker-compose build
  ```

  ## 啟動前端、後端、DB
  ```
  docker-compose up
  ```
  
  ## 常用指令
  啟動backend, frontend, db
  ```
  docker-compose up
  ```

  關掉container
  ```
  docker-compose stop
  ```

  docker frontend怪怪的可以重新build試試看
  ```
  docker-compose build frontend
  ```

  想執行任何指令
  ```
  # container沒開時
  docker-compose run --rm frontend <你的指令>

  # container開啟時
  docker exec -it kyj_stream_frontend_1 <你的指令>
  ```

  進入container的bash terminal
  ```
  在container已啟動的情況下，開啟另一個terminal並輸入指令
  docker exec -it kyj_stream_frontend_1 bash
  ```

  當整個docker變得很怪的時候，清除所有image和volume
  ```
  docker-compose stop
  docker system prune -af --volumes
  ```
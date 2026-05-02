# タスク管理アプリ

## 概要

Flaskを用いて作成したタスク管理アプリです。
CRUD（追加・表示・編集・削除）機能を実装しています。

## 使用技術

* Python
* Flask
* SQLite
* Bootstrap

## 機能

* タスクの追加
* タスクの編集
* タスクの削除
* タスク一覧表示

## 工夫した点

* SQLiteを使用し、データの永続化を実現
* POST後にリダイレクトすることで二重送信を防止
* Bootstrapを使用してUIを改善

## 起動方法

pip install -r requirements.txt
python app.py

## 今後の改善

* ログイン機能の追加
* バリデーション強化

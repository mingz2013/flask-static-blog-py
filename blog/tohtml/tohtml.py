# -*- coding: utf-8 -*-
"""
@FileName: tohtml
@Time: 2020/3/6 14:24
@Author: zhaojm

Module Description

"""
import json
import os


def do_asserts(asserts_path):
    pass


def do_image(image_path):
    pass


def do_md(markdown_path):
    pass


def do_article(category_path, json_file_path):
    """
    处理一篇文章
    """
    meta = json.load(open(json_file_path, 'r'))

    acticle_slug = meta['slug']
    asserts_path = os.path.join(category_path, acticle_slug)
    do_asserts(asserts_path)

    acticle_img = meta['img']
    image_path = os.path.join(category_path, acticle_img)
    do_image(image_path)

    acticle_md = meta['markdown']
    markdown_path = os.path.join(category_path, acticle_md)
    do_md(markdown_path)


def do_category(category_path):
    """
    处理category目录
    """
    dir_or_files = os.listdir(category_path)
    for dir_or_file in dir_or_files:
        dir_or_file_path = os.path.join(category_path, dir_or_file)

        if os.path.isfile(dir_or_file_path):
            if dir_or_file_path.split('.')[-1] == 'json':
                do_article(category_path, dir_or_file)


def do_articles(articles_path):
    """
    处理文章目录
    """
    dir_or_files = os.listdir(articles_path)
    for dir_or_file in dir_or_files:
        dir_or_file_path = os.path.join(articles_path, dir_or_file)

        if os.path.isdir(dir_or_file_path):
            do_category(dir_or_file_path)


def do_content(content_path):
    """
    处理content目录
    """
    articles_path = os.path.join(content_path, 'articles')
    do_articles(articles_path)


def to_html():
    """
    to html
    """
    content_path = "../content"
    do_content(content_path)

# 公式のPostgreSQLイメージをベースとして使用
FROM postgres:latest

# 環境変数の設定
ENV DEBIAN_FRONTEND=noninteractive \
    POSTGRES_DB=nutritional_management

# 必要なパッケージや拡張機能のインストール
RUN apt-get update && \
    apt-get install -y tzdata && \
    ln -fs /usr/share/zoneinfo/Asia/Tokyo /etc/localtime && \
    dpkg-reconfigure --frontend noninteractive tzdata && \
    apt-get clean && \
    rm -rf /var/lib/apt/lists/*


FROM rust:latest

# クロス環境のインストール
RUN apt update && apt install -y g++-arm-linux-gnueabihf libc6-dev-armhf-cross
RUN rustup target add armv7-unknown-linux-gnueabihf
RUN rustup toolchain install stable-armv7-unknown-linux-gnueabihf

WORKDIR /work

# リンカーの指定
ENV CARGO_TARGET_ARMV7_UNKNOWN_LINUX_GNUEABIHF_LINKER=arm-linux-gnueabihf-gcc

CMD [ "cargo", "build", "--target", "armv7-unknown-linux-gnueabihf" ]

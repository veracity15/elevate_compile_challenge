FROM redhat/ubi9:9.6-1754586119

RUN dnf install -y \
      cmake \
      gcc \
      gcc-c++ \
      libpng-devel \
      libzstd-devel \
      python3-devel \
      wget \
      zlib-devel

# TODO: Compile libtiff here with the flags: -D zstd=ON -D CMAKE_INSTALL_PREFIX=/usr/

COPY --link . /app
WORKDIR /app

# TODO: Figure out why pillow fails to compile
RUN python3 -m pip install --no-binary Pillow .[dev]

CMD ["pytest", "src/test_app.py"]

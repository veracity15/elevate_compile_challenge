FROM redhat/ubi9:9.6-1754586119

RUN dnf install -y \
      cmake \
      gcc \
      gcc-c++ \
      libpng-devel \
      libjpeg-devel \
      libzstd-devel \
      python3-devel \
      wget \
      zlib-devel

RUN wget https://download.osgeo.org/libtiff/tiff-4.7.1.tar.gz
RUN tar -xzf tiff-4.7.1.tar.gz
WORKDIR tiff-4.7.1
# Making tiff in the /usr/ folder and using zstd
RUN cmake -D zstd=ON -D CMAKE_INSTALL_PREFIX=/usr/ 
RUN make
RUN make test
RUN make install


COPY --link . /app
WORKDIR /app

RUN python3 -m pip install --no-binary Pillow Pillow
RUN python3 -m pip install Flask pytest

CMD ["pytest", "src/test_app.py"]

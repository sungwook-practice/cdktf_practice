FROM nikolaik/python-nodejs:python3.9-nodejs20-slim

RUN apt-get update && \
    apt-get install -y vim git unzip curl

# install tfenv
ARG TF_VERSION="1.4.0"
RUN git clone --depth=1 https://github.com/tfutils/tfenv.git ~/.tfenv && \
    echo 'export PATH="$HOME/.tfenv/bin:$PATH"' > /etc/profile.d/tfenv.sh && \
    $HOME/.tfenv/bin/tfenv install $TF_VERSION && \
    $HOME/.tfenv/bin/tfenv use $TF_VERSION

# install awscli
RUN curl "https://awscli.amazonaws.com/awscli-exe-linux-x86_64.zip" -o "awscliv2.zip" && \
    unzip awscliv2.zip && \
    ./aws/install && \
    rm -rf ./awscliv2.zip

# install cdktf
ARG CDKTF_VERSION="0.16.1"
RUN apt-get -y install make g++ && \
    npm install --global "cdktf-cli@$CDKTF_VERSION"
#
# This file is auto-generated. DO NOT EDIT
# Generated by: autospec.py
# Using build pattern: cmake
# autospec version: v20
# autospec commit: b2d28bb55a98
#
Name     : mbedtls
Version  : 3.6.2
Release  : 7
URL      : https://github.com/Mbed-TLS/mbedtls/releases/download/mbedtls-3.6.2/mbedtls-3.6.2.tar.bz2
Source0  : https://github.com/Mbed-TLS/mbedtls/releases/download/mbedtls-3.6.2/mbedtls-3.6.2.tar.bz2
Summary  : @PKGCONFIG_PROJECT_DESCRIPTION@
Group    : Development/Tools
License  : Apache-2.0
Requires: mbedtls-bin = %{version}-%{release}
Requires: mbedtls-lib = %{version}-%{release}
Requires: mbedtls-license = %{version}-%{release}
BuildRequires : buildreq-cmake
BuildRequires : glibc-dev
BuildRequires : perl
BuildRequires : python3
BuildRequires : python3-dev
# Suppress stripping binaries
%define __strip /bin/true
%define debug_package %{nil}
Patch1: mbedtls-gcc14.patch

%description
The documents in this directory are proposed specifications for Mbed
TLS features. They are not implemented yet, or only partially
implemented. Please follow activity on the `development` branch of
Mbed TLS if you are interested in these features.

%package bin
Summary: bin components for the mbedtls package.
Group: Binaries
Requires: mbedtls-license = %{version}-%{release}

%description bin
bin components for the mbedtls package.


%package dev
Summary: dev components for the mbedtls package.
Group: Development
Requires: mbedtls-lib = %{version}-%{release}
Requires: mbedtls-bin = %{version}-%{release}
Provides: mbedtls-devel = %{version}-%{release}
Requires: mbedtls = %{version}-%{release}

%description dev
dev components for the mbedtls package.


%package lib
Summary: lib components for the mbedtls package.
Group: Libraries
Requires: mbedtls-license = %{version}-%{release}

%description lib
lib components for the mbedtls package.


%package license
Summary: license components for the mbedtls package.
Group: Default

%description license
license components for the mbedtls package.


%prep
%setup -q -n mbedtls-3.6.2
cd %{_builddir}/mbedtls-3.6.2
%patch -P 1 -p1
pushd ..
cp -a mbedtls-3.6.2 buildavx2
popd

%build
export http_proxy=http://127.0.0.1:9/
export https_proxy=http://127.0.0.1:9/
export no_proxy=localhost,127.0.0.1,0.0.0.0
export LANG=C.UTF-8
export SOURCE_DATE_EPOCH=1729120766
mkdir -p clr-build
pushd clr-build
export GCC_IGNORE_WERROR=1
export AR=gcc-ar
export RANLIB=gcc-ranlib
export NM=gcc-nm
CLEAR_INTERMEDIATE_CFLAGS="$CLEAR_INTERMEDIATE_CFLAGS -O3 -fdebug-types-section -femit-struct-debug-baseonly -ffat-lto-objects -flto=auto -g1 -gno-column-info -gno-variable-location-views -gz=zstd "
CLEAR_INTERMEDIATE_FCFLAGS="$CLEAR_INTERMEDIATE_FFLAGS -O3 -fdebug-types-section -femit-struct-debug-baseonly -ffat-lto-objects -flto=auto -g1 -gno-column-info -gno-variable-location-views -gz=zstd "
CLEAR_INTERMEDIATE_FFLAGS="$CLEAR_INTERMEDIATE_FFLAGS -O3 -fdebug-types-section -femit-struct-debug-baseonly -ffat-lto-objects -flto=auto -g1 -gno-column-info -gno-variable-location-views -gz=zstd "
CLEAR_INTERMEDIATE_CXXFLAGS="$CLEAR_INTERMEDIATE_CXXFLAGS -O3 -fdebug-types-section -femit-struct-debug-baseonly -ffat-lto-objects -flto=auto -g1 -gno-column-info -gno-variable-location-views -gz=zstd "
CFLAGS="$CLEAR_INTERMEDIATE_CFLAGS"
CXXFLAGS="$CLEAR_INTERMEDIATE_CXXFLAGS"
FFLAGS="$CLEAR_INTERMEDIATE_FFLAGS"
FCFLAGS="$CLEAR_INTERMEDIATE_FCFLAGS"
ASFLAGS="$CLEAR_INTERMEDIATE_ASFLAGS"
LDFLAGS="$CLEAR_INTERMEDIATE_LDFLAGS"
export GOAMD64=v2
%cmake .. -DUSE_SHARED_MBEDTLS_LIBRARY=On  -G 'Unix Makefiles'
make  %{?_smp_mflags}
popd
pushd ../buildavx2/
mkdir -p clr-build-avx2
pushd clr-build-avx2
export GCC_IGNORE_WERROR=1
export AR=gcc-ar
export RANLIB=gcc-ranlib
export NM=gcc-nm
CLEAR_INTERMEDIATE_CFLAGS="$CLEAR_INTERMEDIATE_CFLAGS -O3 -fdebug-types-section -femit-struct-debug-baseonly -ffat-lto-objects -flto=auto -g1 -gno-column-info -gno-variable-location-views -gz=zstd "
CLEAR_INTERMEDIATE_FCFLAGS="$CLEAR_INTERMEDIATE_FFLAGS -O3 -fdebug-types-section -femit-struct-debug-baseonly -ffat-lto-objects -flto=auto -g1 -gno-column-info -gno-variable-location-views -gz=zstd "
CLEAR_INTERMEDIATE_FFLAGS="$CLEAR_INTERMEDIATE_FFLAGS -O3 -fdebug-types-section -femit-struct-debug-baseonly -ffat-lto-objects -flto=auto -g1 -gno-column-info -gno-variable-location-views -gz=zstd "
CLEAR_INTERMEDIATE_CXXFLAGS="$CLEAR_INTERMEDIATE_CXXFLAGS -O3 -fdebug-types-section -femit-struct-debug-baseonly -ffat-lto-objects -flto=auto -g1 -gno-column-info -gno-variable-location-views -gz=zstd "
CFLAGS="$CLEAR_INTERMEDIATE_CFLAGS"
CXXFLAGS="$CLEAR_INTERMEDIATE_CXXFLAGS"
FFLAGS="$CLEAR_INTERMEDIATE_FFLAGS"
FCFLAGS="$CLEAR_INTERMEDIATE_FCFLAGS"
ASFLAGS="$CLEAR_INTERMEDIATE_ASFLAGS"
LDFLAGS="$CLEAR_INTERMEDIATE_LDFLAGS"
GOAMD64=v3
CFLAGS="$CLEAR_INTERMEDIATE_CFLAGS -march=x86-64-v3 -Wl,-z,x86-64-v3 "
CXXFLAGS="$CLEAR_INTERMEDIATE_CXXFLAGS -march=x86-64-v3 -Wl,-z,x86-64-v3 "
FFLAGS="$CLEAR_INTERMEDIATE_FFLAGS -march=x86-64-v3 -Wl,-z,x86-64-v3 "
FCFLAGS="$CLEAR_INTERMEDIATE_FCFLAGS -march=x86-64-v3 "
%cmake .. -DUSE_SHARED_MBEDTLS_LIBRARY=On  -G 'Unix Makefiles'
make  %{?_smp_mflags}
popd
popd

%check
export LANG=C.UTF-8
export http_proxy=http://127.0.0.1:9/
export https_proxy=http://127.0.0.1:9/
export no_proxy=localhost,127.0.0.1,0.0.0.0
cd clr-build; make test || :
cd ../../buildavx2/clr-build-avx2;
make test || : || :

%install
export GCC_IGNORE_WERROR=1
export AR=gcc-ar
export RANLIB=gcc-ranlib
export NM=gcc-nm
CLEAR_INTERMEDIATE_CFLAGS="$CLEAR_INTERMEDIATE_CFLAGS -O3 -fdebug-types-section -femit-struct-debug-baseonly -ffat-lto-objects -flto=auto -g1 -gno-column-info -gno-variable-location-views -gz=zstd "
CLEAR_INTERMEDIATE_FCFLAGS="$CLEAR_INTERMEDIATE_FFLAGS -O3 -fdebug-types-section -femit-struct-debug-baseonly -ffat-lto-objects -flto=auto -g1 -gno-column-info -gno-variable-location-views -gz=zstd "
CLEAR_INTERMEDIATE_FFLAGS="$CLEAR_INTERMEDIATE_FFLAGS -O3 -fdebug-types-section -femit-struct-debug-baseonly -ffat-lto-objects -flto=auto -g1 -gno-column-info -gno-variable-location-views -gz=zstd "
CLEAR_INTERMEDIATE_CXXFLAGS="$CLEAR_INTERMEDIATE_CXXFLAGS -O3 -fdebug-types-section -femit-struct-debug-baseonly -ffat-lto-objects -flto=auto -g1 -gno-column-info -gno-variable-location-views -gz=zstd "
CFLAGS="$CLEAR_INTERMEDIATE_CFLAGS"
CXXFLAGS="$CLEAR_INTERMEDIATE_CXXFLAGS"
FFLAGS="$CLEAR_INTERMEDIATE_FFLAGS"
FCFLAGS="$CLEAR_INTERMEDIATE_FCFLAGS"
ASFLAGS="$CLEAR_INTERMEDIATE_ASFLAGS"
LDFLAGS="$CLEAR_INTERMEDIATE_LDFLAGS"
export SOURCE_DATE_EPOCH=1729120766
rm -rf %{buildroot}
mkdir -p %{buildroot}/usr/share/package-licenses/mbedtls
cp %{_builddir}/mbedtls-%{version}/LICENSE %{buildroot}/usr/share/package-licenses/mbedtls/6b0e2c9e46c5cfcddfd028f7014f4f7d4a4ed99d || :
cp %{_builddir}/mbedtls-%{version}/framework/LICENSE %{buildroot}/usr/share/package-licenses/mbedtls/723a807dff6b462c9f9e9496048d82da8b822d89 || :
export GOAMD64=v2
pushd ../buildavx2/
GOAMD64=v3
pushd clr-build-avx2
%make_install_v3  || :
popd
popd
GOAMD64=v2
pushd clr-build
%make_install
popd
/usr/bin/elf-move.py avx2 %{buildroot}-v3 %{buildroot} %{buildroot}/usr/share/clear/filemap/filemap-%{name}

%files
%defattr(-,root,root,-)

%files bin
%defattr(-,root,root,-)
/V3/usr/bin/aead_demo
/V3/usr/bin/benchmark
/V3/usr/bin/cert_app
/V3/usr/bin/cert_req
/V3/usr/bin/cert_write
/V3/usr/bin/cipher_aead_demo
/V3/usr/bin/crl_app
/V3/usr/bin/crypt_and_hash
/V3/usr/bin/crypto_examples
/V3/usr/bin/dh_client
/V3/usr/bin/dh_genprime
/V3/usr/bin/dh_server
/V3/usr/bin/dtls_client
/V3/usr/bin/dtls_server
/V3/usr/bin/ecdh_curve25519
/V3/usr/bin/ecdsa
/V3/usr/bin/gen_entropy
/V3/usr/bin/gen_key
/V3/usr/bin/gen_random_ctr_drbg
/V3/usr/bin/generic_sum
/V3/usr/bin/hello
/V3/usr/bin/hmac_demo
/V3/usr/bin/key_app
/V3/usr/bin/key_app_writer
/V3/usr/bin/key_ladder_demo
/V3/usr/bin/load_roots
/V3/usr/bin/md_hmac_demo
/V3/usr/bin/metatest
/V3/usr/bin/mini_client
/V3/usr/bin/mpi_demo
/V3/usr/bin/pem2der
/V3/usr/bin/pk_decrypt
/V3/usr/bin/pk_encrypt
/V3/usr/bin/pk_sign
/V3/usr/bin/pk_verify
/V3/usr/bin/psa_constant_names
/V3/usr/bin/psa_hash
/V3/usr/bin/query_compile_time_config
/V3/usr/bin/query_included_headers
/V3/usr/bin/req_app
/V3/usr/bin/rsa_decrypt
/V3/usr/bin/rsa_encrypt
/V3/usr/bin/rsa_genkey
/V3/usr/bin/rsa_sign
/V3/usr/bin/rsa_sign_pss
/V3/usr/bin/rsa_verify
/V3/usr/bin/rsa_verify_pss
/V3/usr/bin/selftest
/V3/usr/bin/ssl_client1
/V3/usr/bin/ssl_client2
/V3/usr/bin/ssl_context_info
/V3/usr/bin/ssl_fork_server
/V3/usr/bin/ssl_mail_client
/V3/usr/bin/ssl_pthread_server
/V3/usr/bin/ssl_server
/V3/usr/bin/ssl_server2
/V3/usr/bin/strerror
/V3/usr/bin/udp_proxy
/V3/usr/bin/zeroize
/usr/bin/aead_demo
/usr/bin/benchmark
/usr/bin/cert_app
/usr/bin/cert_req
/usr/bin/cert_write
/usr/bin/cipher_aead_demo
/usr/bin/crl_app
/usr/bin/crypt_and_hash
/usr/bin/crypto_examples
/usr/bin/dh_client
/usr/bin/dh_genprime
/usr/bin/dh_server
/usr/bin/dtls_client
/usr/bin/dtls_server
/usr/bin/ecdh_curve25519
/usr/bin/ecdsa
/usr/bin/gen_entropy
/usr/bin/gen_key
/usr/bin/gen_random_ctr_drbg
/usr/bin/generic_sum
/usr/bin/hello
/usr/bin/hmac_demo
/usr/bin/key_app
/usr/bin/key_app_writer
/usr/bin/key_ladder_demo
/usr/bin/key_ladder_demo.sh
/usr/bin/load_roots
/usr/bin/md_hmac_demo
/usr/bin/metatest
/usr/bin/mini_client
/usr/bin/mpi_demo
/usr/bin/pem2der
/usr/bin/pk_decrypt
/usr/bin/pk_encrypt
/usr/bin/pk_sign
/usr/bin/pk_verify
/usr/bin/psa_constant_names
/usr/bin/psa_hash
/usr/bin/query_compile_time_config
/usr/bin/query_included_headers
/usr/bin/req_app
/usr/bin/rsa_decrypt
/usr/bin/rsa_encrypt
/usr/bin/rsa_genkey
/usr/bin/rsa_sign
/usr/bin/rsa_sign_pss
/usr/bin/rsa_verify
/usr/bin/rsa_verify_pss
/usr/bin/selftest
/usr/bin/ssl_client1
/usr/bin/ssl_client2
/usr/bin/ssl_context_info
/usr/bin/ssl_fork_server
/usr/bin/ssl_mail_client
/usr/bin/ssl_pthread_server
/usr/bin/ssl_server
/usr/bin/ssl_server2
/usr/bin/strerror
/usr/bin/udp_proxy
/usr/bin/zeroize

%files dev
%defattr(-,root,root,-)
/V3/usr/lib64/libeverest.so
/V3/usr/lib64/libp256m.so
/usr/include/everest/Hacl_Curve25519.h
/usr/include/everest/everest.h
/usr/include/everest/kremlib.h
/usr/include/everest/kremlib/FStar_UInt128.h
/usr/include/everest/kremlib/FStar_UInt64_FStar_UInt32_FStar_UInt16_FStar_UInt8.h
/usr/include/everest/kremlin/c_endianness.h
/usr/include/everest/kremlin/internal/builtin.h
/usr/include/everest/kremlin/internal/callconv.h
/usr/include/everest/kremlin/internal/compat.h
/usr/include/everest/kremlin/internal/debug.h
/usr/include/everest/kremlin/internal/target.h
/usr/include/everest/kremlin/internal/types.h
/usr/include/everest/kremlin/internal/wasmsupport.h
/usr/include/everest/vs2013/Hacl_Curve25519.h
/usr/include/everest/vs2013/inttypes.h
/usr/include/everest/vs2013/stdbool.h
/usr/include/everest/x25519.h
/usr/include/mbedtls/aes.h
/usr/include/mbedtls/aria.h
/usr/include/mbedtls/asn1.h
/usr/include/mbedtls/asn1write.h
/usr/include/mbedtls/base64.h
/usr/include/mbedtls/bignum.h
/usr/include/mbedtls/block_cipher.h
/usr/include/mbedtls/build_info.h
/usr/include/mbedtls/camellia.h
/usr/include/mbedtls/ccm.h
/usr/include/mbedtls/chacha20.h
/usr/include/mbedtls/chachapoly.h
/usr/include/mbedtls/check_config.h
/usr/include/mbedtls/cipher.h
/usr/include/mbedtls/cmac.h
/usr/include/mbedtls/compat-2.x.h
/usr/include/mbedtls/config_adjust_legacy_crypto.h
/usr/include/mbedtls/config_adjust_legacy_from_psa.h
/usr/include/mbedtls/config_adjust_psa_from_legacy.h
/usr/include/mbedtls/config_adjust_psa_superset_legacy.h
/usr/include/mbedtls/config_adjust_ssl.h
/usr/include/mbedtls/config_adjust_x509.h
/usr/include/mbedtls/config_psa.h
/usr/include/mbedtls/constant_time.h
/usr/include/mbedtls/ctr_drbg.h
/usr/include/mbedtls/debug.h
/usr/include/mbedtls/des.h
/usr/include/mbedtls/dhm.h
/usr/include/mbedtls/ecdh.h
/usr/include/mbedtls/ecdsa.h
/usr/include/mbedtls/ecjpake.h
/usr/include/mbedtls/ecp.h
/usr/include/mbedtls/entropy.h
/usr/include/mbedtls/error.h
/usr/include/mbedtls/gcm.h
/usr/include/mbedtls/hkdf.h
/usr/include/mbedtls/hmac_drbg.h
/usr/include/mbedtls/lms.h
/usr/include/mbedtls/mbedtls_config.h
/usr/include/mbedtls/md.h
/usr/include/mbedtls/md5.h
/usr/include/mbedtls/memory_buffer_alloc.h
/usr/include/mbedtls/net_sockets.h
/usr/include/mbedtls/nist_kw.h
/usr/include/mbedtls/oid.h
/usr/include/mbedtls/pem.h
/usr/include/mbedtls/pk.h
/usr/include/mbedtls/pkcs12.h
/usr/include/mbedtls/pkcs5.h
/usr/include/mbedtls/pkcs7.h
/usr/include/mbedtls/platform.h
/usr/include/mbedtls/platform_time.h
/usr/include/mbedtls/platform_util.h
/usr/include/mbedtls/poly1305.h
/usr/include/mbedtls/private_access.h
/usr/include/mbedtls/psa_util.h
/usr/include/mbedtls/ripemd160.h
/usr/include/mbedtls/rsa.h
/usr/include/mbedtls/sha1.h
/usr/include/mbedtls/sha256.h
/usr/include/mbedtls/sha3.h
/usr/include/mbedtls/sha512.h
/usr/include/mbedtls/ssl.h
/usr/include/mbedtls/ssl_cache.h
/usr/include/mbedtls/ssl_ciphersuites.h
/usr/include/mbedtls/ssl_cookie.h
/usr/include/mbedtls/ssl_ticket.h
/usr/include/mbedtls/threading.h
/usr/include/mbedtls/timing.h
/usr/include/mbedtls/version.h
/usr/include/mbedtls/x509.h
/usr/include/mbedtls/x509_crl.h
/usr/include/mbedtls/x509_crt.h
/usr/include/mbedtls/x509_csr.h
/usr/include/psa/build_info.h
/usr/include/psa/crypto.h
/usr/include/psa/crypto_adjust_auto_enabled.h
/usr/include/psa/crypto_adjust_config_dependencies.h
/usr/include/psa/crypto_adjust_config_key_pair_types.h
/usr/include/psa/crypto_adjust_config_synonyms.h
/usr/include/psa/crypto_builtin_composites.h
/usr/include/psa/crypto_builtin_key_derivation.h
/usr/include/psa/crypto_builtin_primitives.h
/usr/include/psa/crypto_compat.h
/usr/include/psa/crypto_config.h
/usr/include/psa/crypto_driver_common.h
/usr/include/psa/crypto_driver_contexts_composites.h
/usr/include/psa/crypto_driver_contexts_key_derivation.h
/usr/include/psa/crypto_driver_contexts_primitives.h
/usr/include/psa/crypto_extra.h
/usr/include/psa/crypto_legacy.h
/usr/include/psa/crypto_platform.h
/usr/include/psa/crypto_se_driver.h
/usr/include/psa/crypto_sizes.h
/usr/include/psa/crypto_struct.h
/usr/include/psa/crypto_types.h
/usr/include/psa/crypto_values.h
/usr/lib64/cmake/MbedTLS/MbedTLSConfig.cmake
/usr/lib64/cmake/MbedTLS/MbedTLSConfigVersion.cmake
/usr/lib64/cmake/MbedTLS/MbedTLSTargets-relwithdebinfo.cmake
/usr/lib64/cmake/MbedTLS/MbedTLSTargets.cmake
/usr/lib64/libeverest.so
/usr/lib64/libmbedcrypto.so
/usr/lib64/libmbedtls.so
/usr/lib64/libmbedx509.so
/usr/lib64/libp256m.so
/usr/lib64/pkgconfig/mbedcrypto.pc
/usr/lib64/pkgconfig/mbedtls.pc
/usr/lib64/pkgconfig/mbedx509.pc

%files lib
%defattr(-,root,root,-)
/V3/usr/lib64/libmbedcrypto.so.3.6.2
/V3/usr/lib64/libmbedtls.so.3.6.2
/V3/usr/lib64/libmbedx509.so.3.6.2
/usr/lib64/libmbedcrypto.so.16
/usr/lib64/libmbedcrypto.so.3.6.2
/usr/lib64/libmbedtls.so.21
/usr/lib64/libmbedtls.so.3.6.2
/usr/lib64/libmbedx509.so.3.6.2
/usr/lib64/libmbedx509.so.7

%files license
%defattr(0644,root,root,0755)
/usr/share/package-licenses/mbedtls/6b0e2c9e46c5cfcddfd028f7014f4f7d4a4ed99d
/usr/share/package-licenses/mbedtls/723a807dff6b462c9f9e9496048d82da8b822d89

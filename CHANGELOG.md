# Changelog

## 0.3.2 (2023-10-27)

Full Changelog: [v0.3.1...v0.3.2](https://github.com/Finch-API/finch-api-python/compare/v0.3.1...v0.3.2)

### Chores

* **internal:** minor restructuring of base client ([#158](https://github.com/Finch-API/finch-api-python/issues/158)) ([4aee7a7](https://github.com/Finch-API/finch-api-python/commit/4aee7a757122de18ee54ccecc5a5698e19511aaf))

## 0.3.1 (2023-10-27)

Full Changelog: [v0.3.0...v0.3.1](https://github.com/Finch-API/finch-api-python/compare/v0.3.0...v0.3.1)

## 0.3.0 (2023-10-27)

Full Changelog: [v0.2.3...v0.3.0](https://github.com/finch-api/finch-api-python/compare/v0.2.3...v0.3.0)

### Features

* **client:** adjust retry behavior to be exponential backoff ([#149](https://github.com/finch-api/finch-api-python/issues/149)) ([6c76643](https://github.com/finch-api/finch-api-python/commit/6c766434ba25b5684c41261dfd68355ea9c347ad))
* **client:** improve file upload types ([#148](https://github.com/finch-api/finch-api-python/issues/148)) ([7f9db48](https://github.com/finch-api/finch-api-python/commit/7f9db48ced6c9914cc65ad6e071f3e10ec02885c))
* **client:** support accessing raw response objects ([#154](https://github.com/finch-api/finch-api-python/issues/154)) ([10638eb](https://github.com/finch-api/finch-api-python/commit/10638eb2689ce1a4a522c989df8a9a474e0590f8))


### Chores

* **internal:** require explicit overrides ([#153](https://github.com/finch-api/finch-api-python/issues/153)) ([9ffdf66](https://github.com/finch-api/finch-api-python/commit/9ffdf669051d12e34078205d49d12b7c55909611))


### Documentation

* improve to dictionary example ([#151](https://github.com/finch-api/finch-api-python/issues/151)) ([098d453](https://github.com/finch-api/finch-api-python/commit/098d453e1f1170d14362090500c460fba36d70e9))

## 0.2.3 (2023-10-20)

Full Changelog: [v0.2.2...v0.2.3](https://github.com/Finch-API/finch-api-python/compare/v0.2.2...v0.2.3)

### Chores

* **internal:** bump mypy ([#147](https://github.com/Finch-API/finch-api-python/issues/147)) ([da22ad6](https://github.com/Finch-API/finch-api-python/commit/da22ad671a2d6c3779283aade3e27af8bfd2024e))
* **internal:** bump pyright ([#145](https://github.com/Finch-API/finch-api-python/issues/145)) ([8d62f69](https://github.com/Finch-API/finch-api-python/commit/8d62f69efd62ca6df00cda8af30655fde1e2f0f0))

## 0.2.2 (2023-10-19)

Full Changelog: [v0.2.1...v0.2.2](https://github.com/Finch-API/finch-api-python/compare/v0.2.1...v0.2.2)

## 0.2.1 (2023-10-19)

Full Changelog: [v0.2.0...v0.2.1](https://github.com/Finch-API/finch-api-python/compare/v0.2.0...v0.2.1)

### Chores

* **internal:** update gitignore ([#141](https://github.com/Finch-API/finch-api-python/issues/141)) ([f4325e8](https://github.com/Finch-API/finch-api-python/commit/f4325e83bc9c96578b55c65ede49b95b6c0bfc5e))
* **internal:** update gitignore ([#142](https://github.com/Finch-API/finch-api-python/issues/142)) ([c5cb20a](https://github.com/Finch-API/finch-api-python/commit/c5cb20a35900618e865ab599a8401d87a174045e))
* **internal:** update lock file ([#139](https://github.com/Finch-API/finch-api-python/issues/139)) ([17c0b12](https://github.com/Finch-API/finch-api-python/commit/17c0b125bb03a6d9ef6657a01b67ce680b76ce5d))

## 0.2.0 (2023-10-17)

Full Changelog: [v0.1.5...v0.2.0](https://github.com/Finch-API/finch-api-python/compare/v0.1.5...v0.2.0)

### Features

* **client:** add logging setup ([#127](https://github.com/Finch-API/finch-api-python/issues/127)) ([71aab4b](https://github.com/Finch-API/finch-api-python/commit/71aab4bab20f465005c6300bdedf46862d7fdb82))
* **client:** add support for passing in a httpx client ([#123](https://github.com/Finch-API/finch-api-python/issues/123)) ([623f5bc](https://github.com/Finch-API/finch-api-python/commit/623f5bc8c460e8e880ebc932c8a0f4a4ba780396))
* **client:** support passing httpx.URL instances to base_url ([#138](https://github.com/Finch-API/finch-api-python/issues/138)) ([0aad4df](https://github.com/Finch-API/finch-api-python/commit/0aad4df2c3a86f60ff9a28fc7b28ea2012541257))
* make webhook headers case insensitive ([#130](https://github.com/Finch-API/finch-api-python/issues/130)) ([3af34f9](https://github.com/Finch-API/finch-api-python/commit/3af34f9a71dde0fa60ac7c2aa75e1273e8431015))


### Bug Fixes

* **client:** accept io.IOBase instances in file params ([#134](https://github.com/Finch-API/finch-api-python/issues/134)) ([1297832](https://github.com/Finch-API/finch-api-python/commit/1297832b447ed973ab39b93a329550151747a899))
* **client:** correctly handle arguments with env vars ([#128](https://github.com/Finch-API/finch-api-python/issues/128)) ([e502b18](https://github.com/Finch-API/finch-api-python/commit/e502b18337da39095aee811ea3d69576085602a4))
* correct benfits to benefits ([#125](https://github.com/Finch-API/finch-api-python/issues/125)) ([9e2c02a](https://github.com/Finch-API/finch-api-python/commit/9e2c02ad1f53d94ed523e340751b39f10ebbe483))


### Chores

* **internal:** cleanup some redundant code ([#133](https://github.com/Finch-API/finch-api-python/issues/133)) ([88e49bc](https://github.com/Finch-API/finch-api-python/commit/88e49bcc474195cde09d127d028e3a427b13e9a2))
* **internal:** enable lint rule ([#132](https://github.com/Finch-API/finch-api-python/issues/132)) ([8e266e8](https://github.com/Finch-API/finch-api-python/commit/8e266e82511822cfefc7d877300382a05ca2f25e))
* **internal:** improve publish script ([#137](https://github.com/Finch-API/finch-api-python/issues/137)) ([78cd8ba](https://github.com/Finch-API/finch-api-python/commit/78cd8bad7146ab40a16342d9d0c838d36c041c23))
* **internal:** migrate from Poetry to Rye ([#136](https://github.com/Finch-API/finch-api-python/issues/136)) ([ac49d7c](https://github.com/Finch-API/finch-api-python/commit/ac49d7cd8721c46ad2a1ed77c5f5b75eca7ad4f9))
* update comment ([#131](https://github.com/Finch-API/finch-api-python/issues/131)) ([20aa00a](https://github.com/Finch-API/finch-api-python/commit/20aa00ac06e4104b74c047cc75720b2aa77c2f4a))


### Documentation

* organisation -&gt; organization (UK to US English) ([#135](https://github.com/Finch-API/finch-api-python/issues/135)) ([2e278bd](https://github.com/Finch-API/finch-api-python/commit/2e278bd482dc7407689142037df9fd3bfa15f05e))


### Refactors

* **test:** refactor authentication tests ([#126](https://github.com/Finch-API/finch-api-python/issues/126)) ([88b79b5](https://github.com/Finch-API/finch-api-python/commit/88b79b5a98bda98ae1b6562b385db6ca53105707))

## 0.1.5 (2023-10-09)

Full Changelog: [v0.1.4...v0.1.5](https://github.com/Finch-API/finch-api-python/compare/v0.1.4...v0.1.5)

### Features

* **client:** add forwards-compatible pydantic methods ([#121](https://github.com/Finch-API/finch-api-python/issues/121)) ([b03289d](https://github.com/Finch-API/finch-api-python/commit/b03289d43c95ae13ea16ad3b23cd967d1a28ec34))

## 0.1.4 (2023-10-04)

Full Changelog: [v0.1.3...v0.1.4](https://github.com/Finch-API/finch-api-python/compare/v0.1.3...v0.1.4)

### Features

* **api:** add `/forward` endpoint and other updates ([#116](https://github.com/Finch-API/finch-api-python/issues/116)) ([ef97220](https://github.com/Finch-API/finch-api-python/commit/ef9722064915cbf6f646df514c1a35914a8b2b3f))
* **client:** handle retry-after header with a date format ([#113](https://github.com/Finch-API/finch-api-python/issues/113)) ([b90cd33](https://github.com/Finch-API/finch-api-python/commit/b90cd335063941a7a58a8d93f065f6bcaf310238))


### Chores

* **docs:** adjust some docstrings ([#117](https://github.com/Finch-API/finch-api-python/issues/117)) ([7b68074](https://github.com/Finch-API/finch-api-python/commit/7b6807452c519b2734b2056e48e8592291821752))
* **docs:** adjust some docstrings ([#119](https://github.com/Finch-API/finch-api-python/issues/119)) ([0b9561d](https://github.com/Finch-API/finch-api-python/commit/0b9561d1377930da45d3b816308b630827109dd3))
* **tests:** improve raw response test ([#110](https://github.com/Finch-API/finch-api-python/issues/110)) ([a54268b](https://github.com/Finch-API/finch-api-python/commit/a54268bec11f79d4421af583fb2743ff078eed92))
* **tests:** update test examples ([#118](https://github.com/Finch-API/finch-api-python/issues/118)) ([03a9546](https://github.com/Finch-API/finch-api-python/commit/03a954632c55be84ea4b37f1d69b16aa7199909e))

## 0.1.3 (2023-09-25)

Full Changelog: [v0.1.2...v0.1.3](https://github.com/Finch-API/finch-api-python/compare/v0.1.2...v0.1.3)

### Features

* **ci:** add reviewers ([#106](https://github.com/Finch-API/finch-api-python/issues/106)) ([6cced26](https://github.com/Finch-API/finch-api-python/commit/6cced26464cfd952be880617e0b1fd8321d4ecff))
* **package:** export a root error type ([#108](https://github.com/Finch-API/finch-api-python/issues/108)) ([9ddf707](https://github.com/Finch-API/finch-api-python/commit/9ddf707ef7480471ee19e8fa426c47a3232ad736))


### Bug Fixes

* **client:** don't error by default for unexpected content types ([#104](https://github.com/Finch-API/finch-api-python/issues/104)) ([61dd6ba](https://github.com/Finch-API/finch-api-python/commit/61dd6ba7db2c872d6b234dad3a5abd8a3299cb86))


### Chores

* **internal:** move error classes from _base_exceptions to _exceptions (⚠️ breaking) ([#107](https://github.com/Finch-API/finch-api-python/issues/107)) ([6f6c4a1](https://github.com/Finch-API/finch-api-python/commit/6f6c4a14052fcfba58c8ef9c990f5a7817a59a24))

## 0.1.2 (2023-09-19)

Full Changelog: [v0.1.1...v0.1.2](https://github.com/Finch-API/finch-api-python/compare/v0.1.1...v0.1.2)

### Features

* **client:** retry on 408 Request Timeout ([#99](https://github.com/Finch-API/finch-api-python/issues/99)) ([f8d0bbf](https://github.com/Finch-API/finch-api-python/commit/f8d0bbf9f9f3bd310d4d0cad6f4f43f0a2393273))


### Bug Fixes

* **client:** properly configure model set fields ([#98](https://github.com/Finch-API/finch-api-python/issues/98)) ([ada3ad6](https://github.com/Finch-API/finch-api-python/commit/ada3ad60c40e1b26fcb0a12be0686df82f523554))


### Chores

* **api:** remove deprecated & unused ATS API ([#103](https://github.com/Finch-API/finch-api-python/issues/103)) ([96b9a92](https://github.com/Finch-API/finch-api-python/commit/96b9a923ef83207e9b3c20676cde3690a4c368d6))
* **internal:** add helpers ([#100](https://github.com/Finch-API/finch-api-python/issues/100)) ([fec8c01](https://github.com/Finch-API/finch-api-python/commit/fec8c01ac4bee0f2a39ed42e0b4d6b2bf170ebf1))


### Documentation

* add some missing inline documentation ([#95](https://github.com/Finch-API/finch-api-python/issues/95)) ([dc178c6](https://github.com/Finch-API/finch-api-python/commit/dc178c60adc0e38291c94d2d9e5347b528e4edbe))

## 0.1.1 (2023-09-11)

Full Changelog: [v0.1.0...v0.1.1](https://github.com/Finch-API/finch-api-python/compare/v0.1.0...v0.1.1)

### Features

* add webhook verification methods ([#89](https://github.com/Finch-API/finch-api-python/issues/89)) ([483ffef](https://github.com/Finch-API/finch-api-python/commit/483ffefdaf118a1f9d496dfb5309ced17fe1ffb5))


### Bug Fixes

* **client:** properly handle optional file params ([#88](https://github.com/Finch-API/finch-api-python/issues/88)) ([77b9914](https://github.com/Finch-API/finch-api-python/commit/77b991409d71ca0e608082f54c00824f00d0841d))
* **pagination:** don't duplicate shared types ([#86](https://github.com/Finch-API/finch-api-python/issues/86)) ([3f5d18f](https://github.com/Finch-API/finch-api-python/commit/3f5d18f2a71488e6d5248acaed8e9b68c1d6a15d))


### Chores

* **internal:** add example for configuration ([#81](https://github.com/Finch-API/finch-api-python/issues/81)) ([a71605a](https://github.com/Finch-API/finch-api-python/commit/a71605a090760aa91120c16265f81bd742376d04))
* **internal:** minor formatting changes ([#87](https://github.com/Finch-API/finch-api-python/issues/87)) ([f940fb2](https://github.com/Finch-API/finch-api-python/commit/f940fb2320ce901025eb34f6fbab42a70f80dd37))
* **internal:** minor restructuring ([#84](https://github.com/Finch-API/finch-api-python/issues/84)) ([fafab61](https://github.com/Finch-API/finch-api-python/commit/fafab61d4b247255be99c3c57d7e8975c8ee73ad))
* **internal:** minor update ([#91](https://github.com/Finch-API/finch-api-python/issues/91)) ([1bd2f68](https://github.com/Finch-API/finch-api-python/commit/1bd2f68229cb690b04b2610f0e3bc7cc7c8932d4))
* **internal:** update base client ([#90](https://github.com/Finch-API/finch-api-python/issues/90)) ([ee7284a](https://github.com/Finch-API/finch-api-python/commit/ee7284a84d96158765307011cf8a674b17579894))
* **internal:** update pyright ([#94](https://github.com/Finch-API/finch-api-python/issues/94)) ([9209bca](https://github.com/Finch-API/finch-api-python/commit/9209bca492b41adbd91b00f13d48570e44954e1e))
* **internal:** updates ([#93](https://github.com/Finch-API/finch-api-python/issues/93)) ([01662d9](https://github.com/Finch-API/finch-api-python/commit/01662d9c27a615ae0a638a55df606a77bc98ccbb))


### Documentation

* **readme:** add link to api.md ([#92](https://github.com/Finch-API/finch-api-python/issues/92)) ([4770119](https://github.com/Finch-API/finch-api-python/commit/477011938cf7128f06364fa69db8dd9fa244f5b8))
* **readme:** reference pydantic helpers ([#85](https://github.com/Finch-API/finch-api-python/issues/85)) ([95d0870](https://github.com/Finch-API/finch-api-python/commit/95d087023e69a17aabcc18521078ee2fad106bf7))

## 0.1.0 (2023-08-29)

Full Changelog: [v0.0.11...v0.1.0](https://github.com/Finch-API/finch-api-python/compare/v0.0.11...v0.1.0)

### ⚠ BREAKING CHANGES

* **client:** restructure some methods ([#80](https://github.com/Finch-API/finch-api-python/issues/80))

### Features

* **client:** restructure some methods ([#80](https://github.com/Finch-API/finch-api-python/issues/80)) ([21abe3d](https://github.com/Finch-API/finch-api-python/commit/21abe3d79c572eb6cb232edac37b2d89bf3061e8))


### Chores

* **ci:** setup workflows to create releases and release PRs ([#77](https://github.com/Finch-API/finch-api-python/issues/77)) ([2af3cc1](https://github.com/Finch-API/finch-api-python/commit/2af3cc1013ba8ceb409699a17058a758ae9916ca))

## [0.0.11](https://github.com/Finch-API/finch-api-python/compare/v0.0.10...v0.0.11) (2023-08-26)


### Chores

* **internal:** remove reviewer ([#74](https://github.com/Finch-API/finch-api-python/issues/74)) ([2dfb7fa](https://github.com/Finch-API/finch-api-python/commit/2dfb7fae29910aa164a9ff3dbd708189afb9b2ff))

## [0.0.10](https://github.com/Finch-API/finch-api-python/compare/v0.0.9...v0.0.10) (2023-08-24)


### Chores

* **internal:** bump pydantic dep ([#69](https://github.com/Finch-API/finch-api-python/issues/69)) ([a8f406f](https://github.com/Finch-API/finch-api-python/commit/a8f406fe52ad5e5594f7b595a9c033db0d771e7c))
* **internal:** update anyio ([#71](https://github.com/Finch-API/finch-api-python/issues/71)) ([a5a05af](https://github.com/Finch-API/finch-api-python/commit/a5a05af8964b90a4494cc01faca58f6259dacd58))

## [0.0.9](https://github.com/Finch-API/finch-api-python/compare/v0.0.8...v0.0.9) (2023-08-17)


### Features

* add support for Pydantic v2 ([#66](https://github.com/Finch-API/finch-api-python/issues/66)) ([85d7032](https://github.com/Finch-API/finch-api-python/commit/85d7032f70ae6bd294d96916a91eb42c57a4f6ed))

## [0.0.8](https://github.com/Finch-API/finch-api-python/compare/v0.0.7...v0.0.8) (2023-08-16)


### Features

* allow a default timeout to be set for clients ([#61](https://github.com/Finch-API/finch-api-python/issues/61)) ([0ac3cc6](https://github.com/Finch-API/finch-api-python/commit/0ac3cc62589f8ee0a1152fcaa242106cdfbdeae4))


### Documentation

* **readme:** remove beta status + document versioning policy ([#54](https://github.com/Finch-API/finch-api-python/issues/54)) ([a749f3e](https://github.com/Finch-API/finch-api-python/commit/a749f3edae42ea0b025be4966cd0907600c238e5))


### Styles

* prefer importing types directly instead of module names ([#62](https://github.com/Finch-API/finch-api-python/issues/62)) ([f7dfd51](https://github.com/Finch-API/finch-api-python/commit/f7dfd513c4e88dbed9b10ed6f37830fcf0c07762))


### Chores

* assign default reviewers to release PRs ([#63](https://github.com/Finch-API/finch-api-python/issues/63)) ([502f5c5](https://github.com/Finch-API/finch-api-python/commit/502f5c53bcfff104ea961977b273ffa07594913c))
* **deps:** bump typing-extensions to 4.5 ([#59](https://github.com/Finch-API/finch-api-python/issues/59)) ([d489180](https://github.com/Finch-API/finch-api-python/commit/d489180f9d9ccc748c945be549585937c8a9fc5b))
* **internal/deps:** update lock file ([#58](https://github.com/Finch-API/finch-api-python/issues/58)) ([a5511cf](https://github.com/Finch-API/finch-api-python/commit/a5511cf43a9629d1cd7fd33fbd76be71c22c6215))
* **internal:** bump certifi dependency ([#56](https://github.com/Finch-API/finch-api-python/issues/56)) ([b9506e9](https://github.com/Finch-API/finch-api-python/commit/b9506e96129b867d2fa26836feccb9549602c6ef))
* **internal:** bump lock file ([#53](https://github.com/Finch-API/finch-api-python/issues/53)) ([39d2f3f](https://github.com/Finch-API/finch-api-python/commit/39d2f3fcb929c93e6fdc434c7e64914f606447ae))
* **internal:** bump pytest-asyncio ([#60](https://github.com/Finch-API/finch-api-python/issues/60)) ([4160d43](https://github.com/Finch-API/finch-api-python/commit/4160d43c3df4da4d435862364e3a0cc7b57b5776))
* **internal:** minor formatting change ([#64](https://github.com/Finch-API/finch-api-python/issues/64)) ([aff405c](https://github.com/Finch-API/finch-api-python/commit/aff405cf043ac05b3b1fb1351b7700f29eb24e3c))
* **internal:** minor import restructuring ([#57](https://github.com/Finch-API/finch-api-python/issues/57)) ([bead8c1](https://github.com/Finch-API/finch-api-python/commit/bead8c1eb95b468985545e636df6d81ac14aa16c))
* **internal:** update mypy to v1.4.1 ([#51](https://github.com/Finch-API/finch-api-python/issues/51)) ([9427d13](https://github.com/Finch-API/finch-api-python/commit/9427d13d5f2baec5fd5de52711210c33daf9f271))
* **internal:** update ruff to v0.0.282 ([#55](https://github.com/Finch-API/finch-api-python/issues/55)) ([0f311c4](https://github.com/Finch-API/finch-api-python/commit/0f311c4e0ac5c0a81e2b9a2ff7364b1831ca02e4))

## [0.0.7](https://github.com/Finch-API/finch-api-python/compare/v0.0.6...v0.0.7) (2023-08-01)


### Documentation

* **readme:** use `client` everywhere for consistency ([5a2c941](https://github.com/Finch-API/finch-api-python/commit/5a2c941e02c068fa9d3da1665099f1657812c1ea))


### Chores

* **internal:** bump pyright ([#48](https://github.com/Finch-API/finch-api-python/issues/48)) ([36353e3](https://github.com/Finch-API/finch-api-python/commit/36353e36693a2ee73cc2d745f893c90190235f92))
* **internal:** bump pyright ([#49](https://github.com/Finch-API/finch-api-python/issues/49)) ([bd4d420](https://github.com/Finch-API/finch-api-python/commit/bd4d4207aab19ad76e8d9a520c2c2c2c563b788c))
* **internal:** minor refactoring of client instantiation ([1eff35f](https://github.com/Finch-API/finch-api-python/commit/1eff35f077f28c82fbcc594053d6ecf9088e20e1))
* **internal:** minor reformatting of code ([#46](https://github.com/Finch-API/finch-api-python/issues/46)) ([8ed806e](https://github.com/Finch-API/finch-api-python/commit/8ed806e6c94f0bb315b395d5257ea883401151bc))
* remove unused resource classes ([def0f2e](https://github.com/Finch-API/finch-api-python/commit/def0f2e0a09b99c50ed3aaecb5e5ba0bf22ca618))

## [0.0.6](https://github.com/Finch-API/finch-api-python/compare/v0.0.5...v0.0.6) (2023-07-22)


### Documentation

* **readme:** reference "client" in errors section and add missing import ([#43](https://github.com/Finch-API/finch-api-python/issues/43)) ([3d5a742](https://github.com/Finch-API/finch-api-python/commit/3d5a742ce6b1341377368fd36b092bef024796f3))

## [0.0.5](https://github.com/Finch-API/finch-api-python/compare/v0.0.4...v0.0.5) (2023-07-17)


### Chores

* **internal:** add `codegen.log` to `.gitignore` ([#40](https://github.com/Finch-API/finch-api-python/issues/40)) ([54f5028](https://github.com/Finch-API/finch-api-python/commit/54f50284611843b4a40986d6f553af4e6e5a5198))

## [0.0.4](https://github.com/Finch-API/finch-api-python/compare/v0.0.3...v0.0.4) (2023-07-12)


### Chores

* **package:** pin major versions of dependencies ([#36](https://github.com/Finch-API/finch-api-python/issues/36)) ([e8b1500](https://github.com/Finch-API/finch-api-python/commit/e8b1500ca2c3b309fcc27197b4d5cd76cb42632a))
* **package:** pin major versions of dependencies ([#38](https://github.com/Finch-API/finch-api-python/issues/38)) ([ac82ea9](https://github.com/Finch-API/finch-api-python/commit/ac82ea965df7124d29293fda0af92467a876c03d))

## [0.0.3](https://github.com/Finch-API/finch-api-python/compare/v0.0.2...v0.0.3) (2023-07-07)


### Bug Fixes

* **deps:** pin pydantic to less than v2.0 ([#32](https://github.com/Finch-API/finch-api-python/issues/32)) ([8b7f0df](https://github.com/Finch-API/finch-api-python/commit/8b7f0dffff0a273ae5a5c8e3ce4d48a238e7f8bf))
* **sse:** small improvement to handling server-sent events ([#11](https://github.com/Finch-API/finch-api-python/issues/11)) ([05796db](https://github.com/Finch-API/finch-api-python/commit/05796dbac873826cb5aff667308e45395fe80e34))
* **types:** correct items type for `individuals` arg in `enroll_many` ([#15](https://github.com/Finch-API/finch-api-python/issues/15)) ([3c7b4dd](https://github.com/Finch-API/finch-api-python/commit/3c7b4ddd73ca474303824f6b672614a9e6f7b3a0))


### Styles

* minor reordering of types and properties ([#29](https://github.com/Finch-API/finch-api-python/issues/29)) ([ee4e136](https://github.com/Finch-API/finch-api-python/commit/ee4e1364fc7a7aca22851382e38a3715aabc42e3))


### Documentation

* add trailing newlines ([#28](https://github.com/Finch-API/finch-api-python/issues/28)) ([0f3fb71](https://github.com/Finch-API/finch-api-python/commit/0f3fb71bd87906e38b1323f3ef20155f4216ba99))
* **api.md:** minor restructuring ([#31](https://github.com/Finch-API/finch-api-python/issues/31)) ([69bc6b3](https://github.com/Finch-API/finch-api-python/commit/69bc6b37c22d9eee74966abb4532e161f321ec25))
* point to github repo instead of email contact ([#18](https://github.com/Finch-API/finch-api-python/issues/18)) ([8f21f60](https://github.com/Finch-API/finch-api-python/commit/8f21f60f0c3804e235b38d8409e78bd0b7ac8874))
* **readme:** add note about updating the default version header ([#25](https://github.com/Finch-API/finch-api-python/issues/25)) ([337afec](https://github.com/Finch-API/finch-api-python/commit/337afec18c51b9f0848d3b86ce3ac48dca4641ec))
* **readme:** fix main example snippet ([#23](https://github.com/Finch-API/finch-api-python/issues/23)) ([fb47b35](https://github.com/Finch-API/finch-api-python/commit/fb47b35fd75750d87f1ca168edf105605c4b8842))
* **readme:** update main example ([#21](https://github.com/Finch-API/finch-api-python/issues/21)) ([b15646e](https://github.com/Finch-API/finch-api-python/commit/b15646eeb8eea8d0282a4fa9f5346bf1186d30f2))


### Chores

* **deps:** update certifi ([#27](https://github.com/Finch-API/finch-api-python/issues/27)) ([14d2b06](https://github.com/Finch-API/finch-api-python/commit/14d2b06c5c04b76d0b7ee31da08cc43f9e7e682c))
* **internal:** add empty request preparation method ([#13](https://github.com/Finch-API/finch-api-python/issues/13)) ([601c6ec](https://github.com/Finch-API/finch-api-python/commit/601c6ec23b234a3dfc8b446fb45de8f02721d2d9))
* **internal:** add overloads to `client.get` for streaming ([#19](https://github.com/Finch-API/finch-api-python/issues/19)) ([c1ccaf2](https://github.com/Finch-API/finch-api-python/commit/c1ccaf21fd92a2e8b25d0a863b9955ddc95d5e6c))
* **internal:** add tests for base url handling ([#9](https://github.com/Finch-API/finch-api-python/issues/9)) ([0393cbf](https://github.com/Finch-API/finch-api-python/commit/0393cbfc2b142c41f738de3c49a2585bcd86b7cc))
* **internal:** fix bug with transform utility & key aliases ([#7](https://github.com/Finch-API/finch-api-python/issues/7)) ([c19eb86](https://github.com/Finch-API/finch-api-python/commit/c19eb86f95e099605037b11d9f4dfd992f59bbe0))
* **internal:** fix workflow comment url ([#8](https://github.com/Finch-API/finch-api-python/issues/8)) ([543c6f9](https://github.com/Finch-API/finch-api-python/commit/543c6f997c312813941ffd85d1609ab0d8b7b56c))
* **internal:** improve internal test helper ([#16](https://github.com/Finch-API/finch-api-python/issues/16)) ([a535336](https://github.com/Finch-API/finch-api-python/commit/a535336342c2117d80bc194dd2d48fa45b0225c8))
* **internal:** minor formatting change ([#12](https://github.com/Finch-API/finch-api-python/issues/12)) ([d2610d9](https://github.com/Finch-API/finch-api-python/commit/d2610d9e581abae6f5550bcae48c6964b6048bd5))
* **internal:** restructure core streaming implementation ([#14](https://github.com/Finch-API/finch-api-python/issues/14)) ([5c4a4dd](https://github.com/Finch-API/finch-api-python/commit/5c4a4ddfd26f0d4daa9e653a5cb38b8df9a5663d))
* **internal:** update changelog config ([#5](https://github.com/Finch-API/finch-api-python/issues/5)) ([4c885cf](https://github.com/Finch-API/finch-api-python/commit/4c885cf3a663adf522861b97a25a24971e5f60b7))
* **internal:** update lock file ([#10](https://github.com/Finch-API/finch-api-python/issues/10)) ([11b2ebb](https://github.com/Finch-API/finch-api-python/commit/11b2ebb3408a2e5dbe4e963209b39e2e1f77888c))
* **internal:** update lock file ([#34](https://github.com/Finch-API/finch-api-python/issues/34)) ([772aac0](https://github.com/Finch-API/finch-api-python/commit/772aac00765de0aa0caa1499742ef782ac836a17))

## [0.0.2](https://github.com/Finch-API/finch-api-python/compare/v0.0.1...v0.0.2) (2023-05-08)


### Features

* initial commit ([#1](https://github.com/Finch-API/finch-api-python/issues/1)) ([#2](https://github.com/Finch-API/finch-api-python/issues/2)) ([b64fff9](https://github.com/Finch-API/finch-api-python/commit/b64fff957b170f2719dd14ae5e3987813e9355dd))

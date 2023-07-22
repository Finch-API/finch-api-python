# Changelog

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

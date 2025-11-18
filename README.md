# SHICTHRS ConfigLoader

[![License: GPL v3](https://img.shields.io/badge/License-GPLv3-blue.svg)](https://www.gnu.org/licenses/gpl-3.0)
[![Python Version](https://img.shields.io/badge/python-3.6%2B-blue.svg)](https://www.python.org/downloads/)
[![Version](https://img.shields.io/badge/version-1.1.0-green.svg)](https://github.com/JNTMTMTM/SHICTHRS_ConfigLoader)

SHICTHRS ConfigLoader 是一个轻量级、易于使用的 Python 配置文件读写库，专为处理 INI 格式配置文件而设计。它提供了一个简洁的 API 来读取和写入配置文件，并包含错误处理机制。

## 特性

- 🚀 **轻量高效**：基于原生 Python ConfigParser，无冗余依赖
- 📝 **简单易用**：提供直观的 API，几行代码即可完成配置文件操作
- 🔍 **错误处理**：内置详细的错误处理机制，便于调试
- 🌈 **美观输出**：使用 Colorama 提供彩色终端输出
- 📦 **开箱即用**：支持 UTF-8 编码，处理中文配置项无障碍

## 安装

```bash
pip install SHICTHRSConfigLoader
```

或者从源代码安装：

```bash
git clone https://github.com/JNTMTMTM/SHICTHRS_ConfigLoader.git
cd SHICTHRS_ConfigLoader
pip install -e .
```

## 快速开始

### 读取配置文件

```python
import SHICTHRSConfigLoader.SHICTHRSConfigLoader as config_loader

# 读取配置文件
config = config_loader.SHRConfigLoader_read_ini_file('config.ini')
print(config)
```

### 写入配置文件

```python
import SHICTHRSConfigLoader.SHICTHRSConfigLoader as config_loader

# 定义配置数据
config_data = {
    'database': {
        'host': 'localhost',
        'port': '3306',
        'username': 'admin',
        'password': 'password'
    },
    'application': {
        'debug': 'True',
        'log_level': 'INFO'
    }
}

# 写入配置文件
config_loader.SHRConfigLoader_write_ini_file(config_data, 'config.ini')
```

## API 参考

### `SHRConfigLoader_read_ini_file(path)`

读取指定路径的 INI 配置文件并返回字典格式的配置数据。

**参数：**
- `path` (str): 配置文件路径

**返回：**
- `dict`: 包含所有配置节的字典

**异常：**
- `SHRConfigLoaderException`: 当文件不存在或读取失败时抛出

### `SHRConfigLoader_write_ini_file(config_dict, path)`

将字典格式的配置数据写入指定路径的 INI 配置文件。

**参数：**
- `config_dict` (dict): 配置数据字典
- `path` (str): 要写入的文件路径

**异常：**
- `SHRConfigLoaderException`: 当写入失败时抛出

## 示例配置文件

```ini
[database]
host = localhost
port = 3306
username = admin
password = password

[application]
debug = True
log_level = INFO
```

## 错误处理

SHICTHRS ConfigLoader 提供了详细的错误处理机制：

```python
try:
    config = config_loader.SHRConfigLoader_read_ini_file('nonexistent.ini')
except config_loader.SHRConfigLoaderException as e:
    print(f"配置读取错误: {e}")
```

## 依赖项

- Python 3.6+
- colorama==0.4.6

## 许可证

本项目采用 GPL-3.0 许可证。详情请参阅 [LICENSE](LICENSE) 文件。

## 作者

- **SHICTHRS** - *初始工作* - [JNTMTMTM](https://github.com/JNTMTMTM)

## 贡献

欢迎提交 Issues 和 Pull Requests！

## 支持

如果您在使用过程中遇到问题，请通过以下方式联系：

- 邮箱: contact@shicthrs.com
- GitHub Issues: [https://github.com/JNTMTMTM/SHICTHRS_ConfigLoader/issues](https://github.com/JNTMTMTM/SHICTHRS_ConfigLoader/issues)

---

"Algorithms = rule ; Questioning = approval" - SHICTHRS
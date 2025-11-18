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

### 安装后验证

安装完成后，您可以通过以下方式验证安装是否成功：

```bash
python -c "import SHICTHRSConfigLoader.SHICTHRSConfigLoader as s; print('SHICTHRS ConfigLoader 安装成功!')"
```

您应该看到彩色欢迎信息和"SHICTHRS ConfigLoader 安装成功!"的消息。

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

### 环境模块接口

```python
from SHICTHRSConfigLoader import *
"""
>>> pip install SHICTHRSConfigLoader 后
在环境中调用 SHICTHRSConfigLoader 接口的示例
"""
# 读取文件
SHRConfigLoader_read_ini_file('config.ini')  

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

# 写入文件
SHRConfigLoader_write_ini_file({}, 'config.ini')  
```

## 使用说明

### 完整示例

以下是一个完整的示例，展示了如何创建、读取、修改和保存配置文件：

```python
import SHICTHRSConfigLoader.SHICTHRSConfigLoader as config_loader

# 1. 创建初始配置文件
initial_config = {
    'database': {
        'host': 'localhost',
        'port': '3306',
        'username': 'admin',
        'password': 'password123'
    },
    'application': {
        'name': 'MyApp',
        'version': '1.0.0',
        'debug': 'True'
    },
    'logging': {
        'level': 'INFO',
        'file': 'app.log'
    }
}

# 保存初始配置
config_loader.SHRConfigLoader_write_ini_file(initial_config, 'app_config.ini')
print("配置文件已创建: app_config.ini")

# 2. 读取配置文件
try:
    config = config_loader.SHRConfigLoader_read_ini_file('app_config.ini')
    print("成功读取配置文件:")
    for section, options in config.items():
        print(f"\n[{section}]")
        for key, value in options.items():
            print(f"{key} = {value}")
except config_loader.SHRConfigLoaderException as e:
    print(f"读取配置文件失败: {e}")

# 3. 修改配置
config['application']['debug'] = 'False'  # 修改现有值
config['application']['new_feature'] = 'enabled'  # 添加新键值对
config['new_section'] = {'param1': 'value1', 'param2': 'value2'}  # 添加新节

# 保存修改后的配置
config_loader.SHRConfigLoader_write_ini_file(config, 'app_config.ini')
print("\n配置文件已更新")
```

### 使用技巧

1. **路径处理**: 建议使用绝对路径或确保当前工作目录正确：
   ```python
   import os
   config_path = os.path.join(os.getcwd(), 'config.ini')
   config = config_loader.SHRConfigLoader_read_ini_file(config_path)
   ```

2. **错误处理**: 总是使用 try-except 块来捕获可能的异常：
   ```python
   try:
       config = config_loader.SHRConfigLoader_read_ini_file('config.ini')
   except config_loader.SHRConfigLoaderException as e:
       print(f"配置错误: {e}")
       # 执行适当的错误处理逻辑
   ```

3. **数据类型**: 所有配置值都以字符串形式存储，如需其他类型需要自行转换：
   ```python
   config = config_loader.SHRConfigLoader_read_ini_file('config.ini')
   port = int(config['database']['port'])  # 转换为整数
   debug = config['application']['debug'].lower() == 'true'  # 转换为布尔值
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

- **SHICTHRS** - [JNTMTMTM](https://github.com/JNTMTMTM)

## 贡献

欢迎提交 Issues 和 Pull Requests！

## 支持

如果您在使用过程中遇到问题，请通过以下方式联系：

- 邮箱: contact@shicthrs.com
- GitHub Issues: [https://github.com/JNTMTMTM/SHICTHRS_ConfigLoader/issues](https://github.com/JNTMTMTM/SHICTHRS_ConfigLoader/issues)

---

"Algorithms = rule ; Questioning = approval" - SHICTHRS
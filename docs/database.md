# 数据库

## 用户表 user

表名：`user`

字段：
1. `user_id`：用户id；
2. `user_name`：用户名，登录使用；
3. `nick_name`：昵称名称；
4. `password`：密码；
5. `avatar_src`：头像地址，储存头像图片的链接；
6. `create_time`：创建时间；

### 1. 建表sql
```sql
CREATE TABLE IF NOT  EXISTS `user` (
                `user_id` INT AUTO_INCREMENT PRIMARY KEY,
                `user_name` VARCHAR(50) NOT NULL UNIQUE,
                `nick_name` VARCHAR(100) NOT NULL DEFAULT '',
                `password` VARCHAR(255) NOT NULL,
                `create_time` DATETIME NOT NULL DEFAULT CURRENT_TIMESTAMP
                )
```

### 2. 创建用户sql
```sql
INSERT INTO `user` (
  user_name, 
  nick_name, 
  password, 
  avatar_src
) VALUES (
  'new_user', 
  '小明', 
  'hashed_password_123', 
  'https://example.com/avatar.jpg'
)
```

### 3. 删除用户sql
```sql
DELETE FROM `user` WHERE user_id = ''
```

### 4. 修改用户密码sql
```sql
UPDATE `user`
SET password = '{new_hashed_password}'
WHERE user_id = '{user_id}
```

## 文章分类表 Subset

表名：`subset`

字段：
1. `subset_id`：分类id；
2. `subset_name`：分类名称；

### 1. 建表sql
```sql
CREATE TABLE IF NOT EXISTS `subset` (
  `subset_id` INT NOT NULL AUTO_INCREMENT COMMENT '分类ID（主键）',
  `subset_name` VARCHAR(50) NOT NULL COMMENT '分类名称（唯一）',
  
  PRIMARY KEY (`subset_id`),
  UNIQUE KEY  (`subset_name`) 
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4 COMMENT='分类信息表'
```

### 2. 创建分类sql
```sql
INSERT INTO `subset` (
  subset_name
) VALUES (
  '通知公告', 
)
```

### 3. 删除分类sql
```sql
DELETE FROM `subset` WHERE subset_id = ''
```

### 4. 修改分类名称sql
```sql
UPDATE `subset`
SET subset_name = '{subset_name}'
WHERE subset_id = '{subset_id}
```

## 文章表 article

表名：`article`

字段：
1. `article_id`：文章id；
2. `user_id`：用户id（作者）；外键
3. `subset_id`：文章分类；外键
4. `title`：文章名称；
5. `content`：文章内容；
6. `create_time`：创建时间；
7. `read_count`：阅读量。

### 1. 建表sql
```sql
CREATE TABLE IF NOT EXISTS `article` (
  `article_id` INT NOT NULL AUTO_INCREMENT COMMENT '文章ID（主键）',
  `subset_id` INT NOT NULL COMMENT '文章分类（外键关联 subset 表）',
  `user_id` INT NOT NULL COMMENT '作者用户ID（外键关联 user 表）',
  `title` VARCHAR(255) NOT NULL COMMENT '文章名称',
  `content` TEXT NOT NULL COMMENT '文章内容',
  `create_time` DATETIME NOT NULL DEFAULT CURRENT_TIMESTAMP COMMENT '创建时间',
  `read_count` INT NOT NULL DEFAULT 0 COMMENT '阅读次数（默认0）',
  
  PRIMARY KEY (`article_id`),
  FOREIGN KEY (`user_id`) REFERENCES `user`(`user_id`) ON DELETE CASCADE,
  FOREIGN KEY (`subset_id`) REFERENCES `subset`(`subset_id`) ON DELETE RESTRICT
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4 COMMENT='文章信息表'
```

### 2. 创建文件sql
```sql
INSERT INTO `article` (
  subset_id，
  user_id, 
  title,
  content,
  img_src,
  state
) VALUES (
  
)
```

### 3. 删除文件sql
```sql
DELETE FROM `article` WHERE article_id = ''
```

### 4.增加阅读量
```sql
UPDATE article SET read_count = read_count + 1 WHERE article_id = ''
```
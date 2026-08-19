---
title: "重新启用 gskctl, 一个基于 dsl 的代码生成工具"
source: v2ex
url: "https://www.v2ex.com/t/1231866"
author: "sskycn"
date: 2026-08-03
score: 0
tags: ["代码生成", "AI"]
---

# 重新启用 gskctl, 一个基于 dsl 的代码生成工具

为了确保写出来的代码一定是高效稳定的，我重新启用 gskctl 了。
用 AI 写模板，用它生成代码，好像还不错。
type UserRepository interface {
	// @QueryRow("select * from User where Id = :id")
	GetUser(ctx context.Context, id uint64) (User, error)

	// @Query("select U.Id, U.Name, T.Name as TeamName from User as U left join Team as T where U.Active is true and (U.Name like :name or T.Name is null) order by U.Name limit :limit offset :offset")
	ListUsers(ctx context.Context, name string, limit int, offset int) ([]ListUsersRow, error)

	// @Create("insert into User (Id, Name, Active) values (:id, :name, true) on conflict (Id) do update set Name = excluded.Name returning *")
	UpsertUser(ctx context.Context, id uint64, name string) (User, error)

	// @Update("update User set Name = coalesce(:name, Name) where Id = :id returning Id, Name")

…(内容已截断)

## 涉及话题
- 代码生成
- AI

[原文链接](https://www.v2ex.com/t/1231866)

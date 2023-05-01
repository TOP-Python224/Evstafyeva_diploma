BEGIN;
--
-- Create model Activity
--
CREATE TABLE "users_activity" ("id" integer NOT NULL PRIMARY KEY AUTOINCREMENT,
                               "activity_name" varchar(50) NOT NULL,
                               "burned_calories" integer NOT NULL,
                               "runtime" integer NOT NULL);
--
-- Create model Product
--
CREATE TABLE "users_product" ("id" integer NOT NULL PRIMARY KEY AUTOINCREMENT,
                              "product_name" varchar(50) NOT NULL,
                              "calories" integer NOT NULL,
                              "proteins" integer NOT NULL,
                              "fats" integer NOT NULL,
                              "carbohydrates" integer NOT NULL);
--
-- Create model Reports
--
CREATE TABLE "users_reports" ("id" integer NOT NULL PRIMARY KEY AUTOINCREMENT,
                              "date" date NOT NULL,
                              "water" decimal NOT NULL,
                              "activity_id" smallint NOT NULL
                                    REFERENCES "users_activity" ("id") DEFERRABLE INITIALLY DEFERRED,
                              "product_id" smallint NOT NULL
                                    REFERENCES "users_product" ("id") DEFERRABLE INITIALLY DEFERRED);
--
-- Create model UserData
--
CREATE TABLE "users_userdata" ("id" integer NOT NULL PRIMARY KEY AUTOINCREMENT,
                               "full_name" varchar(100) NOT NULL,
                               "age" integer NOT NULL,
                               "height" integer NOT NULL,
                               "sex" varchar(6) NOT NULL,
                               "purpose" varchar(11) NOT NULL,
                               "activity_level" varchar(9) NOT NULL,
                               "user_id" integer NOT NULL UNIQUE
                                    REFERENCES "auth_user" ("id") DEFERRABLE INITIALLY DEFERRED);
--
-- Create model WeightChange
--
CREATE TABLE "users_weightchange" ("id" integer NOT NULL PRIMARY KEY AUTOINCREMENT,
                                   "date" date NOT NULL,
                                   "weight" decimal NOT NULL,
                                   "bmi" decimal NOT NULL,
                                   "user_data_id" smallint NOT NULL
                                        REFERENCES "users_userdata" ("id") DEFERRABLE INITIALLY DEFERRED);
--
-- Add field user_data to reports
--
CREATE TABLE "new__users_reports" ("id" integer NOT NULL PRIMARY KEY AUTOINCREMENT,
                                   "date" date NOT NULL,
                                   "water" decimal NOT NULL,
                                   "activity_id" smallint NOT NULL
                                        REFERENCES "users_activity" ("id") DEFERRABLE INITIALLY DEFERRED,
                                   "product_id" smallint NOT NULL
                                        REFERENCES "users_product" ("id") DEFERRABLE INITIALLY DEFERRED,
                                   "user_data_id" smallint NOT NULL
                                        REFERENCES "users_userdata" ("id") DEFERRABLE INITIALLY DEFERRED);



INSERT INTO "new__users_reports" ("id", "date", "water", "activity_id", "product_id", "user_data_id") SELECT "id", "date", "water", "activity_id", "product_id", NULL FROM "users_reports";
DROP TABLE "users_reports";
ALTER TABLE "new__users_reports" RENAME TO "users_reports";
CREATE INDEX "users_weightchange_user_data_id_827bd448" ON "users_weightchange" ("user_data_id");
CREATE INDEX "users_reports_activity_id_527d93fc" ON "users_reports" ("activity_id");
CREATE INDEX "users_reports_product_id_92ea5756" ON "users_reports" ("product_id");
CREATE INDEX "users_reports_user_data_id_4d684103" ON "users_reports" ("user_data_id");
COMMIT;

from botcity.core import DesktopBot
from botcity.maestro import *
from botcity.plugins.excel import BotExcelPlugin

import os

# Disable errors if we are not connected to Maestro
BotMaestroSDK.RAISE_NOT_CONNECTED = False

def main():
    # Runner passes the server url, the id of the task being executed,
    # the access token and the parameters that this task receives (when applicable).
    maestro = BotMaestroSDK.from_sys_args()
    ## Fetch the BotExecution with details from the task, including parameters
    execution = maestro.get_execution()
    
    bot = DesktopBot()
    success = 0

    try:
        #path_fakturama = r"C:\Program Files\Fakturama2\Fakturama.exe"
        path_fakturama = execution.parameters.get(r"path_fakturama")
        
        if not os.path.exists(path_fakturama):
            raise FileNotFoundError(f"Fakturama not found: {path_fakturama}")

        bot.execute(path_fakturama)
        product_list = read_excel(r"resources\produtos.xlsx")

        maestro.alert(
            task_id=execution.task_id,
            title="Start process",
            message="This task started to execute.",
            alert_type=AlertType.INFO
        )

        for product in product_list[1:]:
            fill_product(bot, product)     
            success += 1 

            maestro.new_log_entry(
                activity_label="log_product",
                values={
                    "Name": product[1],
                    "Message": "Product registered with success."
                }
            ) 

        status=AutomationTaskFinishStatus.SUCCESS
        message="Task finished with success."
        

    except FileNotFoundError as file_not_found:
        print(file_not_found)
        status=AutomationTaskFinishStatus.FAILED
        message="File not found."

    except Exception as error:
        status=AutomationTaskFinishStatus.FAILED
        message=error

        filepath = bot.save_screenshot()	
        maestro.error(
            task_id=execution.task_id, 
            exception=error, 
            screenshot=filepath
        )

    finally:
        bot.alt_f4()
        maestro.finish_task(
            task_id=execution.task_id,
            status=status,
            message=message,
            total_items=len(product_list)-1,
            processed_items=success,
            failed_items=len(product_list)-1-success
        )

def not_found(label):
    print(f"Element not found: {label}")


def read_excel(fakturama_path):
    bot_excel = BotExcelPlugin()
    bot_excel.read(fakturama_path)

    return bot_excel.as_list()

def fill_product(bot: DesktopBot, product):
    if not bot.find("button_new_product", matching=0.97, waiting_time=100000):
        not_found("button_new_product")
    bot.click()

    if not bot.find("label_item_number", matching=0.97, waiting_time=10000):
        not_found("label_item_number")
    bot.click_relative(107, 6)

    # Preencher Item Number
    bot.paste(product[0])

    # Preencher Name
    bot.tab()
    bot.type_keys(product[1])

    # Preencher category
    bot.tab()
    bot.paste(product[2])

    # Preencher GTIN
    bot.tab()
    bot.paste(product[3])

    # Preencher supplier code
    bot.tab()
    bot.paste(product[4])

    # Preencher Description
    bot.tab()
    bot.paste(product[5])

    # Preencher Price
    bot.tab()
    bot.control_a()
    bot.paste(product[6])

    # Preencher Cost Price
    bot.tab()
    bot.control_a()
    bot.paste(product[7])

    # Preencher Allowance
    bot.tab()
    bot.paste(product[8])

    # Preencher VAT
    bot.tab()

    # Preencher Stock
    bot.tab()
    bot.control_a()
    bot.paste(product[9])

    # Salvar o cadastro
    if not bot.find("button_save", matching=0.97, waiting_time=10000):
        not_found("button_save")
    bot.click()

    bot.control_w()
    

if __name__ == '__main__':
    main()
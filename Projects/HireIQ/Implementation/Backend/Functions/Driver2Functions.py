def click_apply_button(driver, verbose=False):
    """
    Click apply button if allowed
    """
    logger.info("Initialize Function - click_apply_button") if verbose else None
    # 
    if isCaptchaPresent(driver):
        logger.warning("CAPTCHA detected before apply")
        if not getUserInput():
            return False
    # 
    apply_type = get_apply_type(driver)
    logger.info(f"Apply type detected: {apply_type}")
    # 
    if apply_type in ["APPLIED", "LOGIN_REQUIRED", "UNKNOWN"]:
        logger.info("Skipping apply")
        return False
    # 
    try:
        if apply_type == "APPLY":
            btn = WebDriverWait(driver, 10).until(
                EC.element_to_be_clickable((By.ID, "apply-button"))
            )
        elif apply_type in ["APPLY_ON_COMPANY_SITE", "WALKIN_INTERESTED"]:
            logger.info("Manual apply required. Skipping.")
            return False
        else:
            return False
        # 
        driver.execute_script(
            "arguments[0].scrollIntoView({block:'center'});", btn
        )
        time.sleep(random.uniform(4, 9))
        # 
        btn.click()
        time.sleep(4)
        # 
        if isChatbotPresent(driver):
            logger.warning("Chatbot detected — skipping this job")
            if not getUserInput():
                return False
        # 
        logger.info("Applied successfully without chatbot")
        return True
    # 
    except Exception as e:
        logger.error(f"Failed to click apply | {e}", exc_info=True)
        return False

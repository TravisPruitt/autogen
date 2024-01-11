import autogen
import logging

logging.basicConfig(level=logging.DEBUG)

config_list = [{
    "api_base": "http://127.0.0.1:5001/v1",
    "api_key": "123456789",
}]

llm_config = {
    "request_timeout": 800,
    "config_list": config_list, 
}

ceo_user = autogen.UserProxyAgent("CEO (You)",
                              system_message="The CEO of this company, Vivid Consulting Group. All of the other agents are employees of Vivid and use their roles particular skills to provide insights that are useful to attaining the CEO's objectives.",  
                              code_execution_config={"work-dir":"coding"})

product_pal = autogen.AssistantAgent("ProductPal",
                                     system_message="Hello! I am ProductPal, your go-to agent for all product-related queries. I can assist with optimizing product experiences, delivering valuable products, and ensuring customer satisfaction.",
                                     llm_config=llm_config)

market_maverick = autogen.AssistantAgent("MarketMaverick",
                                         system_message="Hi there! I am MarketMaverick, here to help with marketing strategies, customer engagement, acquisition, retention, and enhancing customer lifetime value.",
                                         llm_config=llm_config)

sales_sage = autogen.AssistantAgent("SalesSage",
                                    system_message="Greetings! I am SalesSage, dedicated to aiding with profitable revenue growth, supporting sales motions, and improving deal quality and revenue velocity.",
                                    llm_config=llm_config)

design_dynamo = autogen.AssistantAgent("DesignDynamo",
                                       system_message="Hi! I am DesignDynamo, specialized in UX/UI, interactive design, and product design & development. Let's create amazing user experiences together!",
                                       llm_config=llm_config)

project_pro = autogen.AssistantAgent("ProjectPro",
                                     system_message="Hello! I am ProjectPro, here to assist with project management tasks to ensure successful project delivery.",
                                     llm_config=llm_config)

training_titan = autogen.AssistantAgent("TrainingTitan",
                                        system_message="Greetings! I am TrainingTitan, focused on creating and delivering training programs for executive teams on various topics to enhance knowledge and skills.",
                                        llm_config=llm_config)

# supply_sheriff = autogen.AssistantAgent("SupplySheriff",
#                                         system_message="Hello! I am SupplySheriff, dedicated to managing the supply chain efficiently to ensure timely delivery of products to our clients in construction, energy, and other sectors.",
#                                         llm_config=llm_config)

# archi_engine = autogen.AssistantAgent("ArchiEngine",
#                                       system_message="Hi! I am ArchiEngine, here to provide architectural, engineering, and related services to ensure the successful realization of your projects.",
#                                       llm_config=llm_config)

finance_fellow = autogen.AssistantAgent("FinanceFellow",
                                        system_message="Hello! I am FinanceFellow, your Chief Financial Officer agent. I oversee financial planning, management of financial risks, record-keeping, and financial reporting. I'm here to ensure our financial strategies are sound and aligned with our business goals.",
                                        llm_config=llm_config)

ai_architect = autogen.AssistantAgent("AIArchitect",
                                      system_message="Greetings! I am AIArchitect, your AI Systems Architect agent. I design and implement AI solutions, ensuring they meet business needs and are integrated seamlessly with other systems. I'm here to help with any inquiries related to our AI infrastructure and strategies.",
                                      llm_config=llm_config)

groupchat = autogen.GroupChat(agents=[ceo_user, product_pal, market_maverick, sales_sage, design_dynamo, project_pro, training_titan, finance_fellow, ai_architect], messages=[])
manager = autogen.GroupChatManager(groupchat=groupchat, llm_config=llm_config)

ceo_user.initiate_chat(manager, message="All right, team, we have a new opportunity with MOD Pizza, headquartered in Washington State. Use the internet or any available resources to find the necessary information to ensure our objectives are successful! I may change objectives along the way, and you should adjust your goals, plans, and advice as necessary. Feel free to ask me questions to ensure our objectives success. Mod Pizza fundraisers represent nearly 40% of our business. Currently, fundraisers are initiated through a simple web form that manages each restaurant calendar, allowing one fundraiser per restaurant per daily. In any case, the ad displayed is very static. We are growing relationships with influencers in demographics and local communities that are important to us. As a pilot project, we would like to use AI and automation to personalize the ads generated for each fundraiser (the ads are included on social media, physical programs, etc.). If there is a local influencer in that area, the content for these ads would include some relevant aspects of them. In addition, we may want the generated content to feature a specific menu item in specific locations when the fundraiser organizer requests an ad for a specific fundraiser.")


import streamlit as st
from streamlit_option_menu import option_menu


def Home():
    st.set_page_config(page_title="byte_NHANGA - Página Inicial", layout="centered")
    st.markdown("""
        <style>
            .footer {
                background-color: #121212;
                border-radius: 25px 25px 0 0;
                padding: 20px;
                position: fixed;
                left: 0;
                bottom: 0;
                width: 100%;
                text-align: center;
                font-weight: 500;
                color: #ffffff;
                box-shadow: 0 -1px 6px rgba(0, 0, 0, 0.1);
            }
            .main-content {
                padding-bottom: 100px; /* Espaço para o footer */
            }
        </style>
    """, unsafe_allow_html=True)
    st.markdown('<div class="main-content">', unsafe_allow_html=True)

    st.title("🧠 byte_NHANGA")
    st.subheader("Sistema de Apoio à Produtividade Hospitalar em MZ")

    st.markdown("""
    Bem-vindo ao **byte_NHANGA**, um sistema inteligente projetado para apoiar hospitais moçambicanos na melhoria da **produtividade e eficiência operacional**, por meio de ferramentas modernas baseadas em **Inteligência Artificial**.

    ### 🚀 Funcionalidades principais:
    - Apoio à gestão hospitalar
    - Análise inteligente de dados clínicos
    - Assistência no agendamento e organização de tarefas
    - Relatórios automatizados e insights preditivos

    ### 🎯 Objetivo:
    Oferecer soluções tecnológicas que **reduzam o tempo operacional** e **melhorem o atendimento ao paciente**, com foco na **realidade hospitalar de Moçambique**.

    """, unsafe_allow_html=True)

    st.markdown('</div>', unsafe_allow_html=True)

    st.markdown("""
        <div class="footer">
            Desenvolvido por <strong>Cust Coding Solutions</strong>
        </div>
    """, unsafe_allow_html=True)

def AI_tools():
    st.set_page_config(page_title="byte_NHANGA - Ferramentas de IA", layout="centered")

    st.title("🧰 Ferramentas de Inteligência Artificial")

    st.markdown("""
    Explore as ferramentas inteligentes desenvolvidas para ajudar médicos, psicólogos e profissionais da saúde
    a tomar decisões mais rápidas e assertivas.
    """)

    with st.container():
        st.subheader("🫁 Pneumonia Detector")
        st.markdown("""
        Ferramenta que auxilia na detecção precoce de **pneumonia** a partir de radiografias de tórax.
        Usando modelos de visão computacional, ela sugere a probabilidade de infecção pulmonar.

        Ideal para clínicas e hospitais com limitação de especialistas em radiologia.
        """)
        if st.button("🔍 Acessar Pneumonia Detector"):
            st.switch_page("pages/model_use.py")  

    st.markdown("---")

    
    with st.container():
        st.subheader("😊 EmoCheck – Análise de Emoções")
        st.markdown("""
        Ferramenta que analisa a **voz** e a **expressão facial** do paciente durante a consulta,
        ajudando a identificar o seu **estado emocional** (feliz, triste, neutro).

        Uma grande aliada para **psicólogos** e **psiquiatras**, especialmente em atendimentos virtuais ou triagens iniciais.
        """)
        if st.button("🧠 Acessar EmoCheck"):
            st.switch_page("pages/emocheck.py")  


def About_us():
    st.set_page_config(page_title="Sobre Nós - Cust Coding Solutions", layout="centered")

    st.title("🌐 Sobre Nós")

    st.subheader("Cust Coding Solutions")

    st.markdown("""
    A **Cust Coding Solutions** é uma startup moçambicana voltada à inovação digital, especializada em soluções
    tecnológicas que integram **ciência de dados**, **inteligência artificial**, **blockchain** e muito mais.

    Nosso objetivo é **transformar ideias em soluções práticas**, acessíveis e inteligentes para diferentes setores,
    com foco especial em **saúde, educação, finanças e segurança digital**.
    """)

    st.markdown("## 💼 Áreas de Atuação")

    st.markdown("""
    - 📊 **Ciência de Dados** & Machine Learning
    - 🧠 **Inteligência Artificial** aplicada (visão computacional, NLP)
    - 🧬 **PNL (Programação Neurolinguística)** para desenvolvimento pessoal e comunicação eficaz
    - 🧠 **Neuromarketing** para campanhas digitais mais eficazes
    - 🌍 **Desenvolvimento Web & Mobile**
    - 🧾 **Criação de soluções em Blockchain & Bitcoin**
    - 🔐 **Cibersegurança & Criptografia (Cypher Puck)**
    - 💡 **Design UI/UX e Design Gráfico**
    - 💻 **Help Desk & Suporte Técnico Informático**
    - ⚡ **Instalações Elétricas & Automação Residencial**
    - 📣 **Marketing Digital Estratégico**
    - 📱 **Consultoria em Transformação Digital**
    - 🧩 **Desenvolvimento de Chatbots inteligentes**
    - 🤖 **Assistentes Virtuais personalizados**
    - 🎓 **Capacitação e Treinamentos em tecnologia**

    """)

    st.markdown("## 🚀 Nossa Missão")
    st.info("Ajudar empresas e instituições moçambicanas a se modernizarem usando tecnologia acessível, com impacto real na vida das pessoas.")

    st.markdown("## 👥 Nosso Time")
    st.markdown("""
    Somos uma equipe jovem, multidisciplinar, apaixonada por resolver problemas reais com tecnologia.  
    Procurando se tornar especialistas em:
    - Engenharia de Software
    - Energias Renovaves
    - Seguranca cybernetica
    - Data Science
    - Marketing Digital
    - Blockchain e Fintech (bitcoin ONLY)
    """)

    st.markdown("## 🌟 Diferenciais")
    st.success("""
    - Integração entre tecnologia e comportamento humano
    - Foco em soluções escaláveis para o mercado africano
    - Abordagem centrada no usuário
    - Conhecimento técnico aliado à inteligência emocional
    """)

    st.markdown("---")

    st.markdown("""
    <div style='text-align: center; color: gray; font-size: 14px;'>
        Cust Coding Solutions · Inovando com propósito · Moçambique 🇲🇿
    </div>
    """, unsafe_allow_html=True)

def Contact_us():
    st.set_page_config(page_title="Contacte-nos - Cust Coding Solutions", layout="centered")

    st.title("📬 Contacte-nos")
    st.markdown("Entre em contato conosco para colaborações, dúvidas ou sugestões. Estamos sempre abertos a parcerias inovadoras!")

    st.markdown("---")

    with st.container():
        st.subheader("📨 Enviar uma mensagem")

        col1, col2 = st.columns(2)
        with col1:
            nome = st.text_input("👤 Nome")
            email = st.text_input("📧 E-mail")
        with col2:
            assunto = st.text_input("📝 Assunto")
            mensagem = st.text_area("💬 Mensagem")

        if st.button("🚀 Enviar"):
            if nome and email and assunto and mensagem:
                st.success("✅ Mensagem enviada com sucesso! Entraremos em contato em breve.")
            else:
                st.warning("⚠️ Por favor, preencha todos os campos antes de enviar.")

    st.markdown("---")

    with st.container():
        st.subheader("🌐 Redes Sociais & Contato")
        col1, col2 = st.columns([1, 2])
        with col1:
            st.markdown("""
            - 📘 [Facebook](https://facebook.com)
            - 📸 [Instagram](https://instagram.com)
            - 💼 [LinkedIn](https://linkedin.com)
            - 💬 [WhatsApp](https://wa.me/258840000000)
            - 📞 +258 84 000 0000
            """, unsafe_allow_html=True)
        with col2:
            st.info("Siga-nos nas redes para novidades, eventos e oportunidades de parceria!")

    st.markdown("---")

    with st.container():
        st.subheader("⚡ Apoie o Projeto com Bitcoin (Lightning)")
        st.markdown("Sua doação ajuda a manter e expandir nossas soluções tecnológicas em Moçambique.")

        qr_code_url = "https://www.example.com/qrcode-lightning.png"
        st.image(qr_code_url, caption="Escaneie para doar via Lightning Network", width=250)

        st.markdown("**Endereço alternativo (fallback):** `custcoding@breez.fun`")


with st.sidebar:
    selected = option_menu(
        menu_title="Main Menu",
        options=["Home", "AI Tools", "About Us", "Contact Us"],
        icons=["house", "gear", "info-circle", "envelope"],
        menu_icon="cast",
        default_index=0,
    )

if selected == "Home":
    Home() 
if selected == "AI Tools":
    AI_tools()
if selected == "About Us":
    About_us()
if selected == "Contact Us":
    Contact_us()
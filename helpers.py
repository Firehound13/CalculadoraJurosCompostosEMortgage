def juros_compostos(principal, taxa, periodo):
    """
    Função para calcular juros compostos
    :param principal: float
    :param taxa: float/inteiro
    :param periodo: inteiro
    :return: resultado
    """
    calculo_juros = principal * (pow(1 + taxa / 100), periodo)
    return calculo_juros
